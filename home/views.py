from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from products.models import Product, Genre

import datetime


def determine_new_releases():
    """
    Determines whether product is a new release or not.  Queries whether
    each products release date is within a specific period of time.
    (determined by the 'new_release_time_period' value) and updates the
    product new_release boolean value accordingly.
    https://www.listendata.com/2019/07/how-to-use-datetime-in-python.html#Calculate-future-or-past-dates
    """
    products = Product.objects.all()

    new_release_time_period = 90
    today = datetime.date.today()
    # print(f'Todays date is: {today}')
    delta = datetime.timedelta(days=new_release_time_period)
    past_date = today - delta
    # print(f'the past date is: {past_date}')

    # print('now running updates')
    for product in products:
        if (product.release_date > past_date) and (product.release_date < today):
            this_product = product
            this_product.new_release = True
            this_product.save()
            # print('true')
        else:
            this_product = product
            this_product.new_release = False
            this_product.save()
            # print('false')


def determine_preorders():
    """
    Determines whether product is a pre-order item.  Queries whether
    each products release date is in the future and updates the product
    new_release boolean value accordingly.
    """
    products = Product.objects.all()
    today = datetime.date.today()

    for product in products:
        if product.release_date > today:
            this_product = product
            this_product.pre_order = True
            this_product.save()
            # print("true")
        else:
            this_product = product
            this_product.pre_order = False
            this_product.save()
            # print("False")


def main():
    """
    Functions to be run when site starts
    """
    determine_new_releases()
    determine_preorders()


# main() 


def index(request):
    """
    Home page of site that shows the best selling products initially and
    includes sorting a searching queries.
    """
    products = Product.objects.all()
    per_page = 12
    product_paginator = Paginator(products, per_page)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)

    page_heading = "All Boardgames"
    genre_query = None
    query = None
    # category = None
    chart = False

    if request.GET:
        # requests from 'shop front' menu drop down:
        if 'used' in request.GET:
            page_heading = 'Used Games'
            products = products.filter(used=True)

        if 'on_sale' in request.GET:
            page_heading = 'Currently On Sale!'
            products = products.filter(on_sale=True)

        if 'new' in request.GET:
            determine_new_releases()
            page_heading = 'Latest Releases!'
            products = products.filter(new_release=True)

        if 'preorder' in request.GET:
            determine_preorders()
            page_heading = 'Available for pre-order'
            products = products.filter(pre_order=True)

        if 'bestseller' in request.GET:
            page_heading = 'Current top 10 bestellers'
            products = products.order_by('-sold')
            chart = True

        # requests from 'shop by genre' menu drop down (adapted from Boutique Ado category query):
        if 'genre' in request.GET:
            genre_query = request.GET['genre'].split(',')
            products = products.filter(genre__name__in=genre_query)
            selected_genre = Genre.objects.get(name__in=genre_query)
            page_heading = (selected_genre.friendly_name)

        # Search query function from Boutique Ado walkthrough project
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You need to enter a search value.")
                return redirect(reverse('home'))

            queries = Q(product_name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        product_paginator = Paginator(products, per_page)
        page_num = request.GET.get('page')
        page = product_paginator.get_page(page_num)

    context = {
        'page': page,
        'search_term': query,
        'per_page': per_page,
        # 'current_category': category,
        'heading': page_heading,
        'chart': chart
    }

    return render(request, 'home/index.html', context)
