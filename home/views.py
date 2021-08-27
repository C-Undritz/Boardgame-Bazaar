from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from products.models import Product, Genre

import datetime


def determine_new_releases():
    """
    Determines whether product is a new release or not.  Queries whether
    each products release date is within the last previous period of months
    (determined by the 'new_release_month_period' value) and updates the
    product new_release boolean value accordingly.
    """
    # new_release_month_period = 2
    # products = Product.objects.all()

    # def determine_past_date(value):
    #     return value.replace(month=value.month - new_release_month_period)

    # today = datetime.date.today()
    # past_date = determine_past_date(today)
    # print(f'past date is: {past_date}')

    # for product in products:
    #     if (product.release_date > past_date) and (product.release_date < today):
    #         this_product = product
    #         this_product.new_release = True
    #         this_product.save()
    #         print("true")
    #     else:
    #         this_product = product
    #         this_product.new_release = False
    #         this_product.save()
    #         print("False")

    new_release_month_period = 6
    products = Product.objects.all()

    def determine_past_date(value):
        minus_months = value.replace(month=value.month - new_release_month_period)
        # past_date = minus_months.replace(day=minus_months.day - 5)

        return minus_months

    today = datetime.date.today()
    print(today)
    past_date = determine_past_date(today)
    print(f'past date is: {past_date}')

    ## ----- Code to fix issue -----
    # new_release_month_period = 2
    # products = Product.objects.all()

    # try:
    #     def determine_past_date(value):
    #         return value.replace(month=value.month - new_release_month_period)

    #     today = datetime.date.today()
    #     past_date = determine_past_date(today)
    #     print(f'past date is: {past_date}')
    ## except ValueError as e:
    ##     print(f"Invalid data: {e}, please try again.\n")
    ##     return False
    # except:
    #     def determine_past_date(value):
    #         month_reduction = value.replace(month=value.month - new_release_month_period)
    #         return = month_reduction.replace(day=month_reduction.day - 5)

    #     today = datetime.date.today()
    #     past_date = determine_past_date(today)
    #     print(f'past date is: {past_date}')
    # finally:
    #     for product in products:
    #         if (product.release_date > past_date) and (product.release_date < today):
    #             this_product = product
    #             this_product.new_release = True
    #             this_product.save()
    #             print("true")
    #         else:
    #             this_product = product
    #             this_product.new_release = False
    #             this_product.save()
    #             print("False")

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
    genres = Genre.objects.all()
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
            # determine_new_releases()
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

    context = {
        'products': products,
        'genres': genres,
        'search_term': query,
        # 'current_category': category,
        'heading': page_heading,
        'chart': chart
    }

    return render(request, 'home/index.html', context)
