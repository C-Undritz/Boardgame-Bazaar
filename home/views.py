from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from products.models import Product, Category


def index(request):
    """
    Home page of site that shows the best selling products initially and
    includes sorting a searching queries.
    """
    products = Product.objects.all()
    query = None
    category = None

    # Search query function from Boutique Ado walkthrough project
    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(category__name__in=category)
            category = Category.objects.filter(name__in=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You need to enter a search value.")
                return redirect(reverse('home'))

            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'serach_term': query,
        'current_category': category,
    }

    return render(request, 'home/index.html', context)
