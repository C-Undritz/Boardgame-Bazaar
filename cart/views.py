"""
Boardgame Bazaar: cart App - Views
"""


from django.shortcuts import (
    render, redirect, reverse,
    HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ A view that renders the shopping cart page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add a quantity of a product to the shopping cart.  A bootstrap off-canvas
    is used to display the cart updates to the customer whilst shopping.
    Adapted from the CI Boutique Ado project
    """
    quantity = int(request.POST.get('quantity') or 1)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # Determines if item exists and updates quantity or adds item.
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.add_message(request, 50, 'value')
    else:
        cart[item_id] = quantity
        messages.add_message(request, 50, 'value')

    # Overwrites the cart variable in the session with updated version.
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """
    Updates the quantity of the specified product to a specified amount. User
    should not be able to enter a '0' quantity at any point.  Adapted from
    the CI Boutique Ado project.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity') or 1)
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request,
            f'{product.name.title()} quantity updated to {cart[item_id]}')
    else:
        # Should not be needed; kept in incase scenario not perceived occurs.
        cart.pop(item_id)
        messages.success(request, f'{product.name.title()} removed from cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    Removes the item from the shopping cart. Adapted from the CI Boutique Ado
    project.
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'{product.name.title()} removed from cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
