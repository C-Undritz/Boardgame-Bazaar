"""
Boardgame Bazaar: profiles App - Views
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
    Adds to/removes from the mailing list database, the customer email address
    Initiated by the mailing list subscribe/un-subscribe button within Account
    Management.
    """
    user_profile = get_object_or_404(User, username=request.user)

    if request.method == 'POST':
        if MailingList.objects.all().filter(email=user_profile.email).exists():
            email = get_object_or_404(MailingList, email=user_profile.email)
            email.delete()
            messages.success(request, 'Removed from mailing list')
            return redirect(reverse('profile'))
        else:
            MailingList.objects.create(email=user_profile.email)
            messages.success(request, 'Added to mailing list')
            return redirect(reverse('profile'))


@login_required
def profile(request):
    """
    Returns the User data and mailing list status for display. Processes
    any changes the customer makes to User data.
    """
    user_profile = get_object_or_404(User, username=request.user)
    mailinglist_status = MailingList.objects.all().filter(
        email=user_profile.email).exists()
    previous_email = user_profile.email

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            updated_profile = get_object_or_404(User, username=request.user)
            if previous_email != updated_profile.email:
                email = get_object_or_404(MailingList, email=previous_email)
                email.delete()
                MailingList.objects.create(email=updated_profile.email)
                messages.success(request, 'Account information updated \
                successfully and new email updated in mailing list')
            else:
                messages.success(request, 'Account information updated \
                    successfully')
        else:
            messages.error(request, 'Update failed. Please check that you have \
                filled out all required information')
    else:
        form = UserForm(instance=user_profile)

    template = 'profiles/profile_information.html'
    context = {
        'profile': user_profile,
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
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserAddressForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account information updated \
                successfully')
        else:
            messages.error(request, 'Update failed. Please check that you have \
                filled out all required information')
    else:
        form = UserAddressForm(instance=user_profile)

    template = 'profiles/profile_address.html'
    context = {
        'profile': user_profile,
        'form': form,
    }

    return render(request, template, context)


@login_required
def profile_orders(request):
    """
    Returns the customer account order history.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    orders = user_profile.orders.all()

    template = 'profiles/profile_orders.html'
    context = {
        'profile': user_profile,
        'orders': orders
    }

    return render(request, template, context)


@login_required
def order_detail(request, order_number):
    """
    Returns the order history information for the selected order from the
    order history page.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    order = get_object_or_404(Order, order_number=order_number)

    if str(order.user_profile) != str(request.user):
        messages.warning(request, 'You are not allowed to perform this \
            action.')
        return redirect(reverse('home'))

    template = 'profiles/order_detail.html'
    context = {
        'profile': user_profile,
        'order': order
    }

    return render(request, template, context)


@login_required
def wishlist_toggle(request, product_id, nav):
    """
    Allows the customer to add and removed a product to their wishlist list
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if user_profile.wishlist.filter(id=product_id).exists():
        user_profile.wishlist.remove(product_id)
        messages.success(request, 'Removed from wishlist')
    else:
        user_profile.wishlist.add(product_id)
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
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_wishlist = user_profile.wishlist.filter()

    template = 'profiles/profile_wishlist.html'
    context = {
        'profile': user_profile,
        'wishlist': user_wishlist,
    }

    return render(request, template, context)
