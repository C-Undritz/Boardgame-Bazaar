# Logic and instructions for the stripe elements below can be found here:
# https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
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

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty, please add a game to checkout.")
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
