# Logic and instructions for the stripe elements below can be found here:
# https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from cart.contexts import cart_contents

import stripe


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
        print(cart)

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
            order = order_form.save()
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