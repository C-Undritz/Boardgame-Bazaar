from django.shortcuts import render


def profile(request):
    """
    Displays the user profile page
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
