# Logic and instructions for the stripe elements below can be found here:
# https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserAddressForm
from profiles.models import UserProfile
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def is_in_stock(request):
    """
    At the point of checkout, determines is there is enough stock
    for each item in the cart, by checking with the database stock
    levels.  Purchase will be stopped if the chosen quantity of one
    or more of the items is more than the current stock.
    """
    cart = request.session.get('cart', {})
    confirmed_okay = 0
    for item_id, item_data in cart.items():
        product = Product.objects.get(id=item_id)
        if item_data <= product.stock:
            confirmed_okay += 1
        elif product.pre_order:
            # Allows for the purchase of pre-order items.
            confirmed_okay += 1
        else:
            continue

    if confirmed_okay == len(cart):
        result = True  # this means that sale can complete
    else:
        result = False  # this means that sale cannot complete

    return JsonResponse({'result': result})


def no_sale(request):
    """
    Should there not be enough stock of one or more of the cart items at
    the point of checkout, this function is called to redirect customer
    to the cart and display an appropriate message.
    """
    messages.error(request, (
        "You have selected too many items for one or more of your purchases. \
            Please recheck the displayed stock levels of your selected games. \
                Please do contact us to discuss if you experience further \
                    issues.")
    )
    return redirect(reverse('view_cart'))


@require_POST
def cache_checkout_data(request):
    """
    This function is called before the 'stripe.confirmCardPayment' method in
    JS. It passes the user choice for 'save_info' checkbox on the checkout
    form within the metadata key and attaches it to the PaymentIntent, along
    takes a copy of the session cart and the customer username.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'{e}: Sorry, your payment cannot be processed. \
            Please try again later.')
        return HttpResponse(status=400)


def checkout(request):
    """
    Returns to return the checkout page.  Includes if statement to protect
    against. URL abuse a button to checkout only appears in item(s) in cart.
    Learnt and adapted from Boutique Ado project.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart was not found in \
                            our database."
                        "Please select another game or contact us to discuss.")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
            # checking whether the user wants to save their profile information
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please retry and double check the information entered')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty.")
            return redirect(reverse('home'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        # Multiplied and rounded to zero decimal places as Stripe needs charge amount to be integer.
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # pre-fill delivery information if saved in profile:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    # full name and email from user account
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    # remainder is information from user profile
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                    'phone_number': profile.default_phone_number,
                })
                # if user not authenticated an empty form is rendered
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handles successful checkouts
    """
    # saves to a variable, the users choice to save form information to profile
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the users profile to the order
        order.user_profile = profile
        order.save()

        # save the user's info
        if save_info:
            profile_data = {
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county, 
                'default_postcode': order.postcode,
                'default_country': order.country,
                'default_phone_number': order.phone_number,
            }
            user_address_form = UserAddressForm(profile_data, instance=profile)
            if user_address_form.is_valid():
                user_address_form.save()

    messages.success(request, f'Order successful.  Your order \
        number is {order_number}. A confirmation email will be \
        sent to {order.email}.')

    # deletes session cart
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)