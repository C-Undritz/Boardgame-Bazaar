from django.shortcuts import render, redirect


def view_cart(request):
    """ A view that renders the shopping cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add a quantity of a product to the shopping cart.  Adapted from the CI
    Boutique Ado project
    """
    quantity = int(request.POST.get('quantity'))
    print(f'the item quantity is: {quantity}')
    redirect_url = request.POST.get('redirect_url')
    print(f'the redirect_url is: {redirect_url}')
    # gets session 'cart' variable or creates it
    cart = request.session.get('cart', {})
    print(f'The cart contents is: {cart}')

    # determines if item exists and updates quantity or adds item.
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    print(f'The cart contents is now: {cart}')

    # overwrites the variable in the session with updated version
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
