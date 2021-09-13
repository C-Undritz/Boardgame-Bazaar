from django.shortcuts import render, get_object_or_404

from products.models import Genre
from .models import UserProfile


def profile(request):
    """
    Displays the user profile page
    """
    genres = Genre.objects.all()
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'genres': genres,
        'profile': profile,
    }

    return render(request, template, context)
