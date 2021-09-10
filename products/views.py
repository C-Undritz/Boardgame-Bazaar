from django.shortcuts import render, get_object_or_404
from .models import Product, Genre, GenreAssignment


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
