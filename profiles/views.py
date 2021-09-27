from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product, Genre
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def profile(request):
    """
    Displays the user account deliery and contact information.
    """
    genres = Genre.objects.all()
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, 'Account information updated successfully')
        else:
            messages.error(request, 'Update failed. Please check that you have filled out all required information')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile_information.html'
    context = {
        'genres': genres,
        'profile': profile,
        'form': form,
    }

    return render(request, template, context)

@login_required
def profile_orders(request):
    """
    Displays the user account order history.
    """
    genres = Genre.objects.all()
    profile = get_object_or_404(UserProfile, user=request.user)

    # gets users orders so order history can be displayed
    orders = profile.orders.all()

    template = 'profiles/profile_orders.html'
    context = {
        'genres': genres,
        'profile': profile,
        'orders': orders
    }

    return render(request, template, context)

@login_required
def order_detail(request, order_number):
    """
    Displays information for the selected order from the order history
    page
    """
    genres = Genre.objects.all()
    profile = get_object_or_404(UserProfile, user=request.user)

    order = get_object_or_404(Order, order_number=order_number)

    template = 'profiles/order_detail.html'
    context = {
        'genres': genres,
        'profile': profile,
        'order': order
    }

    return render(request, template, context)

@login_required
def wishlist_toggle(request, product_id):
    """
    Allows the customer to add a product to a wishlist list and 
    remove it if required
    """
    print(product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.wishlist.filter(id=product_id).exists():
        profile.wishlist.remove(product_id)
    else:
        profile.wishlist.add(product_id)
    return redirect(reverse('product_detail', args=[product_id]))
