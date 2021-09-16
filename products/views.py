from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product, Genre, GenreAssignment
from .forms import ProductForm


def product_detail(request, product_id):
    """
    View to show individual product details
    """
    genres = Genre.objects.all()
    product = get_object_or_404(Product, pk=product_id)
    display_genres = GenreAssignment.objects.filter(product=product)
    stock = product.stock
    print(f'product stock is: {stock}')

    context = {
        'product': product,
        'genres': genres,
        'display_genres': display_genres,
        'stock': stock,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """
    Add a product to the store
    """
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
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """
    Edit the details of an existing product
    """
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

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """
    Delete a product from the store
    """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('home'))
