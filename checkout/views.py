from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    Returns to return the checkout page.  Includes if statement to protect
    against. URL abuse a button to checkout only appears in item(s) in cart.
    Learnt and adapted from Boutique Ado project.
    """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty, please add a game to checkout.")
        return redirect(reverse('home'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JL96nDmE8hjt2GqKx5KJ5TC3rrAAsk0rie4qKcbSdr8ry4UUpqT4zxbNEQRicmsKUqerwXCv3SwriX6QVbQqPIh00tPjb9hIL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
