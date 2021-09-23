from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Genre, GenreAssignment
from .forms import ProductForm, UpdateStockForm, ReviewRateForm
from profiles.models import UserProfile


def product_detail(request, product_id):
    """
    View to show individual product details
    """
    genres = Genre.objects.all()
    product = get_object_or_404(Product, pk=product_id)
    display_genres = GenreAssignment.objects.filter(product=product)
    stock = product.stock
    # print(f'product stock is: {stock}')

    context = {
        'product': product,
        'genres': genres,
        'display_genres': display_genres,
        'stock': stock,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """
    Add a product to the store
    """
    genres = Genre.objects.all()
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
        'genres': genres,
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
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
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to edit product. Please check that you have correctly filled out all required information.')
    else:
        form = ProductForm(instance=product)

    genres = Genre.objects.all()
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'genres': genres,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Only authorised staff can perform this function')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('home'))


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

    genres = Genre.objects.all()
    template = 'products/update_stock.html'
    context = {
        'product': product,
        'genres': genres,
        'form': form,
    }

    return render(request, template, context)


@login_required
def review_rate(request, order_ref, product_id):
    """
    Saves user reviews and ratings for a bought product. 
    """
    print(request)
    print(order_ref)
    genres = Genre.objects.all()
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        print('if function called')
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
            return redirect(reverse('order_detail', args=[order_ref]))
        else:
            messages.error(request, 'Failed to add rating and review. Please check that you have correctly filled out all required information.')
    else:
        form = ReviewRateForm()

    template = 'products/review_rate.html'
    context = {
        'product': product,
        'genres': genres,
        'form': form,
        'order_ref': order_ref,
    }

    return render(request, template, context)
