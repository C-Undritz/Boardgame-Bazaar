from django.shortcuts import render, get_object_or_404

from products.models import Genre
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """
    Displays the user profile page.  
    """
    genres = Genre.objects.all()
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=profile)

    # gets users orders so order history can be displayed
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'genres': genres,
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)
