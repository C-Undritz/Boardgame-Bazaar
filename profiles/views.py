from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from products.models import Product, Genre
from checkout.models import Order
from .models import UserProfile
from .forms import UserAddressForm, UserForm


@login_required
def profile(request):
    """
    Displays the user account delivery and contact information.
    """
    profile = get_object_or_404(User, username=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, 'Account information updated successfully')
        else:
            messages.error(request, 'Update failed. Please check that you have filled out all required information')
    else:
        form = UserForm(instance=profile)

    template = 'profiles/profile_information.html'
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, template, context)


@login_required
def profile_address(request):
    """
    Displays the user account delivery address information and phone number.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserAddressForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, 'Account information updated successfully')
        else:
            messages.error(request, 'Update failed. Please check that you have filled out all required information')
    else:
        form = UserAddressForm(instance=profile)

    template = 'profiles/profile_address.html'
    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, template, context)


@login_required
def profile_orders(request):
    """
    Displays the user account order history.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/profile_orders.html'
    context = {
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
    profile = get_object_or_404(UserProfile, user=request.user)
    order = get_object_or_404(Order, order_number=order_number)

    if str(order.user_profile) != str(request.user):
        messages.warning(request, 'You are not allowed to perform this action.')
        return redirect(reverse('home'))

    template = 'profiles/order_detail.html'
    context = {
        'profile': profile,
        'order': order
    }

    return render(request, template, context)

@login_required
def wishlist_toggle(request, product_id, nav):
    """
    Allows the customer to add a product to a wishlist list and
    remove it if required.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if profile.wishlist.filter(id=product_id).exists():
        profile.wishlist.remove(product_id)
        messages.success(request, 'Removed from wishlist')
    else:
        profile.wishlist.add(product_id)
        messages.success(request, 'Added to wishlist')
    if nav:
        return redirect(reverse('product_detail', args=[product_id]))
    else:
        return redirect(reverse('wishlist'))


@login_required
def wishlist(request):
    """
    Displays users current wishlist and allows the deletion
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = profile.wishlist.filter()

    template = 'profiles/profile_wishlist.html'
    context = {
        'profile': profile,
        'wishlist': wishlist,
    }

    return render(request, template, context)