from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from products.models import Product

import datetime


def determine_new_releases():
    """
    Determines whether product is a new release or not.  Queries whether
    each products release date is within the last previous period of months
    (determined by the 'new_release_month_period' value) and updates the
    product new_release boolean value accordingly.
    """
    new_release_month_period = 2
    products = Product.objects.all()

    def determine_past_date(value):
        return value.replace(month=value.month - new_release_month_period)

    today = datetime.date.today()
    past_date = determine_past_date(today)

    for product in products:
        if (product.release_date > past_date) and (product.release_date < today):
            this_product = product
            this_product.new_release = True
            this_product.save()
            print("true")
        else:
            this_product = product
            this_product.new_release = False
            this_product.save()
            print("False")

# functions run when site starts
determine_new_releases()


def index(request):
    """
    Home page of site that shows the best selling products initially and
    includes sorting a searching queries.
    """
    products = Product.objects.all()
    query = None
    category = None
    page_heading = "Best Sellers"

    if request.GET:
        if 'used' in request.GET:
            print('used requested')
            page_heading = 'Used Games'
            products = products.filter(used=True)

        if 'on_sale' in request.GET:
            print('on sale requested')
            page_heading = 'Currently On Sale!'
            products = products.filter(on_sale=True)

        if 'new' in request.GET:
            determine_new_releases()
            print('new releases requested')
            page_heading = 'Latest Releases!'
            products = products.filter(new_release=True)

        # Search query function from Boutique Ado walkthrough project
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You need to enter a search value.")
                return redirect(reverse('home'))

            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
        'heading': page_heading,
    }

    return render(request, 'home/index.html', context)
