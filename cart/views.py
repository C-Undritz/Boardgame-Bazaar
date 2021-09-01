from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Genre, Product


def view_cart(request):
    """ A view that renders the shopping cart page """
    genres = Genre.objects.all()

    context = {
        'genres': genres,
    }

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    """
    Add a quantity of a product to the shopping cart.  Adapted from the CI
    Boutique Ado project
    """
    product = Product.objects.get(pk=items_id)  # retrieved for messages

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})  # gets session 'cart' variable or creates it

    # determines if item exists and updates quantity or adds item.
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to shopping cart')

    # overwrites the variable in the session with updated version
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """
    Updates the quantity of the specified product to a specified amount.
    Adapted from the CI Boutique Ado project
    """
    quantity = int(request.POST.get('quantity'))
    print(f'the item quantity is: {quantity}')
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        print(f'update cart - the cart is: {cart}')
    else:
        cart.pop(item_id)
        print(f'the cart is: {cart}')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    Removes the item from the shopping cart. Adapted from the CI Boutique Ado 
    project.
    """
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        print(e)
        return HttpResponse(status=500)
