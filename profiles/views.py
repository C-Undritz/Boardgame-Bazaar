"""
Boardgame Bazaar: products App - Views
"""


from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from checkout.models import Order
from mailing_list.models import MailingList
from .models import UserProfile
from .forms import UserAddressForm, UserForm


@login_required
def profile_mailinglist(request):
    """
    Checks whether customers email address is already in database
    and returns appropriate response and actions.
    """
    profile = get_object_or_404(User, username=request.user)

    if request.method == 'POST':
        if MailingList.objects.all().filter(email=profile.email).exists():
            email = get_object_or_404(MailingList, email=profile.email)
            email.delete()
            messages.success(request, 'Removed from mailing list')
            return redirect(reverse('profile'))
        else:
            email = MailingList.objects.create(email=profile.email)
            messages.success(request, 'Added to mailing list')
            return redirect(reverse('profile'))


@login_required
def profile(request):
    """
    Returns the User data and mailing list status for display. Processes
    any changes the customer makes to User data.
    """
    profile = get_object_or_404(User, username=request.user)
    mailinglist_status = MailingList.objects.all().filter(
        email=profile.email).exists()

    if request.method == 'POST':
        form = UserForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, 'Account information updated \
                successfully')
        else:
            messages.error(request, 'Update failed. Please check that you have \
                filled out all required information')
    else:
        form = UserForm(instance=profile)

    template = 'profiles/profile_information.html'
    context = {
        'profile': profile,
        'form': form,
        'mailinglist_status': mailinglist_status,
    }

    return render(request, template, context)


@login_required
def profile_address(request):
    """
    Returns the UserProfile data for display. Processes any changes
    the customer makes to UserProfile data.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserAddressForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, 'Account information updated \
                successfully')
        else:
            messages.error(request, 'Update failed. Please check that you have \
                filled out all required information')
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
    Returns the customer account order history.
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
    Returns the order history information for the selected order from the
    order history page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    order = get_object_or_404(Order, order_number=order_number)

    if str(order.user_profile) != str(request.user):
        messages.warning(request, 'You are not allowed to perform this \
            action.')
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
    Allows the customer to add and removed a product to their wishlist list
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
