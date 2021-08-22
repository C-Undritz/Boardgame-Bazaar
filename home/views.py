from django.shortcuts import render
from products.models import Product


def index(request):
    """
    Home page of site that shows the best selling products initially and
    includes sorting a searching queries.
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
