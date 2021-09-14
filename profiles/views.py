from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from products.models import Genre
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


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

    form = UserProfileForm(instance=profile)

    template = 'profiles/profile_information.html'
    context = {
        'genres': genres,
        'profile': profile,
        'form': form,
    }

    return render(request, template, context)


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
