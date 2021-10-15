from django.shortcuts import render


def index(request):
    """ A view that renders the shopping cart page """

    return render(request, 'home/index.html')
