"""
Boardgame Bazaar: home App - Views
"""


from django.shortcuts import render


def index(request):
    """
    Displays the home page.
    """
    return render(request, 'home/index.html')


def aboutus(request):
    """
    Displays the about us information page.
    """
    return render(request, 'home/aboutus.html')


def shipping(request):
    """
    Displays the shipping information page.
    """
    return render(request, 'home/shipping.html')


def returns(request):
    """
    Displays the returns information page.
    """
    return render(request, 'home/returns.html')


def tandcs(request):
    """
    Displays the terms & conditions information page.
    """
    return render(request, 'home/tandcs.html')


def careers(request):
    """
    Displays the careers information page.
    """
    return render(request, 'home/careers.html')


def privacy(request):
    """
    Displays the privacy policy information page.
    """
    return render(request, 'home/privacy.html')
