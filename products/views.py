"""
Boardgame Bazaar: products App - Views
"""


from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from checkout.models import Order
from .models import Product, Genre, GenreAssignment, Review
from .forms import ProductForm, UpdateStockForm, ReviewRateForm, GenreForm


def all_products(request):
    """
    Products display page of site that shows all of the products initially but
    returns various restricted views of the products through filters and
    queries.  Includes sorting by and searching queries.
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
            page_heading = 'Latest Releases!'
            products = products.filter(new_release=True)

        if 'preorder' in request.GET:
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
                return redirect(reverse('all_products'))

            queries = Q(name__icontains=search_query) | Q(
                description__icontains=search_query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': search_query,
        'heading': page_heading,
        'chart': chart,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/all_products.html', context)


def product_detail(request, product_id):
    """
    View to show individual product details where the customer can add the
    product to the shopping cart.
    """
    product = get_object_or_404(Product, pk=product_id)
    display_genres = GenreAssignment.objects.filter(product=product)
    stock = product.stock

    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        if profile.wishlist.filter(id=product_id).exists():
            in_wishlist = True
        else:
            in_wishlist = False
    else:
        in_wishlist = False

    context = {
        'product': product,
        'display_genres': display_genres,
        'stock': stock,
        'in_wishlist': in_wishlist,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Create a new product record in the database. Performs checks on the
    product name to ensure that products with the same name cannot be added.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this \
            function')
        return redirect(reverse('home'))

    if request.method == 'POST':
        product_name = request.POST['name'].lower()
        # Checks whether there is already a product with this name
        if Product.objects.all().filter(name=product_name).exists():
            messages.info(request, 'Product already exists in database')
            return redirect(reverse('add_product'))
        # If there is no duplicate name the new record is permitted
        else:
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save()
                messages.success(request, 'Product added to database')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to add product. Please check \
                    that you have correctly filled out all required \
                        information.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def products_list(request):
    """
    Returns a list of all of the products within the admin view so they can be
    selected to be deleted or edited from the admin menu.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this \
            function')
        return redirect(reverse('home'))

    products = Product.objects.all().order_by('name')
    per_page = 5
    product_paginator = Paginator(products, per_page)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)

    template = 'products/products_list.html'
    context = {
        'page': page,
        'per_page': per_page,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id, nav):
    """
    Edit the details of an existing product. Performs checks on the product
    name to ensure products with the same name cannot be added through the
    editing process.  If the name is the same as the queried product name
    then the save is permitted, so as to allow changes to all product details,
    aside from the name.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this \
            function')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product_name = request.POST['name'].lower()
        # Checks whether there is already a product with this name
        if Product.objects.all().filter(name=product_name).exists():
            # If the name is the same as product name then update permitted
            if product_name == product.name:
                form = ProductForm(
                    request.POST, request.FILES, instance=product)
                if form.is_valid() and nav:
                    form.save()
                    messages.success(request, 'Product successfully updated')
                    return redirect(reverse(
                        'product_detail', args=[product.id]))
                elif form.is_valid():
                    form.save()
                    messages.success(request, 'Product successfully updated')
                    return redirect(reverse('products_list'))
            # update rejected if edited name is same as an existing product
            else:
                messages.info(request, 'Product already exists in database.  \
                    You must have changed the name to another existing \
                        product')
                return redirect(reverse(edit_product, args=[product_id, nav]))
        # If there is no duplicate name the update is permitted
        else:
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid() and nav:
                form.save()
                messages.success(request, 'Product successfully updated')
                return redirect(reverse('product_detail', args=[product.id]))
            elif form.is_valid():
                form.save()
                messages.success(request, 'Product successfully updated')
                return redirect(reverse('products_list'))
            else:
                messages.error(request, 'Failed to edit product. Please check \
                    that you have correctly filled out all required \
                        information.')
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'nav': nav,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id, nav):
    """
    Delete a product from the store.  This function can be accessed from
    the product detail view and also the admin menu.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this \
            function')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')

    if nav:
        return redirect(reverse('home'))
    else:
        return redirect(reverse('products_list'))


@login_required
def add_genre(request):
    """
    Add additional genre category  Performs checks on the genre friendly
    name to ensure duplicate genres cannot be added.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if not request.user.is_superuser:
        messages.error(
            request, 'Only authorised staff can perform this function')
        return redirect(reverse('home'))

    if request.method == 'POST':
        genre_name = request.POST['friendly_name'].lower()
        if Genre.objects.all().filter(friendly_name=genre_name).exists():
            messages.info(
                request, 'Genre with that name already exists in database')
            return redirect(reverse('add_genre'))
        else:
            form = GenreForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'New genre added to database')
                return redirect(reverse('add_genre'))
            else:
                messages.error(request, 'Failed to add genre. Please check \
                    that you have correctly filled out all required \
                        information.')
    else:
        form = GenreForm()

    template = 'products/add_genre.html'
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def genres_list(request):
    """
    Returns a list of all of the genres within the admin view so they can be
    selected to be deleted or edited.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this \
            function')
        return redirect(reverse('home'))

    genres = Genre.objects.all().order_by('friendly_name')
    per_page = 8
    genre_paginator = Paginator(genres, per_page)
    page_num = request.GET.get('page')
    page = genre_paginator.get_page(page_num)

    template = 'products/genres_list.html'
    context = {
        'page': page,
        'per_page': per_page,
    }

    return render(request, template, context)


@login_required
def edit_genre(request, genre_id):
    """
    Edit the details of an existing genre. Performs checks on the genre
    friendly name to ensure duplicate genres cannot be added through the
    editing process.  If the name is the same as the queried product name
    then the save is permitted, so as to allow changes to the other genre
    details, aside from the friendly name.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this \
            function')
        return redirect(reverse('home'))

    genre = get_object_or_404(Genre, pk=genre_id)

    if request.method == 'POST':
        genre_fname = request.POST['friendly_name'].lower()
        if Genre.objects.all().filter(friendly_name=genre_fname).exists():
            if genre_fname == genre.friendly_name:
                form = GenreForm(request.POST, instance=genre)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Genre successfully updated')
                    return redirect(reverse('genres_list'))
            else:
                messages.info(request, 'Genre already exists in database.  You \
                     must have changed the name to another existing genre')
                return redirect(reverse(edit_genre, args=[genre_id]))
        else:
            form = GenreForm(request.POST, instance=genre)
            if form.is_valid():
                form.save()
                messages.success(request, 'Genre successfully updated')
                return redirect(reverse('genres_list'))
            else:
                messages.error(request, 'Failed to edit genre. Please check that \
                    you have correctly filled out all required information.')
    else:
        form = GenreForm(instance=genre)

    template = 'products/edit_genre.html'
    context = {
        'form': form,
        'genre': genre,
    }

    return render(request, template, context)


@login_required
def delete_genre(request, genre_id):
    """
    Delete a genre from the database
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this \
            function')
        return redirect(reverse('home'))

    genre = get_object_or_404(Genre, pk=genre_id)
    genre.delete()
    messages.success(request, 'Genre deleted')

    return redirect(reverse('genres_list'))


@login_required
def update_stock(request, product_id):
    """
    Update product stock function.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this \
            function')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = UpdateStockForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product stock successfully updated')
            return redirect(reverse('update_stock', args=[product.id]))
        else:
            messages.error(request, 'Failed to update stock.  Please check \
                that you have correctly filled out the correct information.')
    else:
        form = UpdateStockForm(instance=product)

    template = 'products/update_stock.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required
def review_rate(request, order_number, product_id):
    """
    Saves user reviews and ratings for a bought product. Checks if user has
    reviewed the product already and if so directs to the edit review function.
    """
    order = get_object_or_404(Order, order_number=order_number)
    # Checks that the user reviewing the product matches order record
    if str(order.user_profile) != str(request.user):
        messages.warning(request, 'You are not allowed to perform this \
            action.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    # Saves the review
    if request.method == 'POST':
        form_data = {
            'rating': request.POST['rating'],
            'review': request.POST['review'],
        }
        review_form = ReviewRateForm(form_data)
        if review_form.is_valid():
            data = review_form.save(commit=False)
            data.user = request.user
            data.product = product
            data.save()
            messages.success(request, 'Review saved.  Thank you!')
            return redirect(reverse('order_detail', args=[order_number]))
        else:
            messages.error(request, 'Failed to add rating and review. Please \
                check that you have correctly filled out all required \
                    information.')
    else:
        reviews = product.reviews.all()
        # Checks if the logged in user has already reviewed the product
        if reviews.filter(user=request.user).exists():
            messages.info(request, 'You have already reviewed this product. \
                You can update or delete your review and rating on this page.')
            return redirect(reverse(
                'edit_review', args=[order_number, product_id]))
        else:
            form = ReviewRateForm()

        template = 'products/review_rate.html'
        context = {
            'product': product,
            'form': form,
            'order_number': order_number,
        }

        return render(request, template, context)


@login_required
def edit_review(request, order_number, product_id):
    """
    Returns the review rate form pre-populated with review data for user to \
    edit or delete.
    """
    order = get_object_or_404(Order, order_number=order_number)
    if str(order.user_profile) != str(request.user):
        messages.warning(request, 'You are not allowed to perform this \
            action.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, user=request.user, product=product_id)
    reviewed = True

    if request.method == 'POST':
        form_data = {
            'rating': request.POST['rating'],
            'review': request.POST['review'],
        }
        review_form = ReviewRateForm(form_data, instance=review)
        if review_form.is_valid():
            data = review_form.save(commit=False)
            data.user = request.user
            data.product = product
            data.save()
            messages.success(request, 'Review successfully updated.')
            return redirect(reverse('order_detail', args=[order_number]))
        else:
            messages.error(request, 'Failed to add rating and review. Please \
                check that you have correctly filled out all required \
                    information.')
    else:
        form = ReviewRateForm()

    template = 'products/review_rate.html'
    context = {
        'product': product,
        'form': form,
        'order_number': order_number,
        'review': review,
        'reviewed': reviewed,
    }

    return render(request, template, context)


@login_required
def delete_review(request, order_number, review_id):
    """
    Deletes a review.
    """
    order = get_object_or_404(Order, order_number=order_number)
    if str(order.user_profile) != str(request.user):
        messages.warning(request, 'You are not allowed to perform this \
            action.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted')

    return redirect(reverse('order_detail', args=[order_number]))
