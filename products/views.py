from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Genre, GenreAssignment, Review
from .forms import ProductForm, UpdateStockForm, ReviewRateForm, GenreForm
from profiles.models import UserProfile


def product_detail(request, product_id):
    """
    View to show individual product details
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
    Add a product to the store
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this function')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added to database')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please check that you have correctly filled out all required information.')
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
        messages.error(request, 'Only authorised staff can perform this function')
        return redirect(reverse('home'))

    products = Product.objects.all().order_by('product_name')

    template = 'products/products_list.html'
    context = {
        'products': products,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id, nav):
    """
    Edit the details of an existing product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this function')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully updated')
            if nav:
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                return redirect(reverse('products_list'))
        else:
            messages.error(request, 'Failed to edit product. Please check that you have correctly filled out all required information.')
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
    Delete a product from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this function')
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
    Add additional genre category
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this function')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New genre added to database')
            return redirect(reverse('add_genre'))
        else:
            messages.error(request, 'Failed to add genre. Please check that you have correctly filled out all required information.')
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
    selected to be deleted or edited.  Uses products > contexts.py to populate
    list.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this function')
        return redirect(reverse('home'))

    template = 'products/genres_list.html'

    return render(request, template)


@login_required
def edit_genre(request, genre_id):
    """
    Edit the details of an existing genre
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this function')
        return redirect(reverse('home'))

    genre = get_object_or_404(Genre, pk=genre_id)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            messages.success(request, 'Genre successfully updated')
            return redirect(reverse('genres_list'))
        else:
            messages.error(request, 'Failed to edit genre. Please check that you have correctly filled out all required information.')
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
    print(f'genre id is: {genre_id}')
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this function')
        return redirect(reverse('home'))

    genre = get_object_or_404(Genre, pk=genre_id)
    genre.delete()
    messages.success(request, 'Genre deleted')

    return redirect(reverse('genres_list'))


@login_required
def update_stock(request, product_id):
    """
    Update product stock function
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this function')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = UpdateStockForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product stock successfully updated')
            return redirect(reverse('update_stock', args=[product.id]))
        else:
            messages.error(request, 'Failed to update stock.  Please check that you have correctly filled out the correct information.')
    else:
        form = UpdateStockForm(instance=product)

    template = 'products/update_stock.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


def edit_review(request, order_number, product_id):
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
            return redirect(reverse('order_detail', args=[order_number]))
        else:
            messages.error(request, 'Failed to add rating and review. Please check that you have correctly filled out all required information.')
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
def review_rate(request, order_number, product_id):
    """
    Saves user reviews and ratings for a bought product. 
    """
    product = get_object_or_404(Product, pk=product_id)
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
            return redirect(reverse('order_detail', args=[order_number]))
        else:
            messages.error(request, 'Failed to add rating and review. Please check that you have correctly filled out all required information.')
    else:
        reviews = product.reviews.all()
        if reviews.filter(user=request.user).exists():
            return redirect(reverse('edit_review', args=[order_number, product_id]))
        else:
            form = ReviewRateForm()
            print('new review')

        template = 'products/review_rate.html'
        context = {
            'product': product,
            'form': form,
            'order_number': order_number,
        }

        return render(request, template, context)
