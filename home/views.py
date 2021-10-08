from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
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


main() 


def index(request):
    """
    Home page of site that shows the best selling products initially and
    includes sorting a searching queries.
    """
    products = Product.objects.all()

    page_heading = "All Boardgames"
    genre_query = None
    search_query = None
    chart = False
    sort = None
    direction = None

    if request.GET:
        # requests from dropdown sort by function
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # requests from 'shop front' menu drop down:
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

        # requests from 'shop by genre' menu drop down:
        if 'genre' in request.GET:
            genre_query = request.GET['genre'].split(',')
            products = products.filter(genre__name__in=genre_query)
            selected_genre = Genre.objects.get(name__in=genre_query)
            page_heading = (selected_genre.friendly_name)

        # Search query function from Boutique Ado walkthrough project
        if 'q' in request.GET:
            search_query = request.GET['q']
            if not search_query:
                messages.error(request, "You need to enter a search value.")
                return redirect(reverse('home'))

            queries = Q(name__icontains=search_query) | Q(description__icontains=search_query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': search_query,
        'heading': page_heading,
        'chart': chart,
        'current_sorting': current_sorting,
    }

    return render(request, 'home/index.html', context)
