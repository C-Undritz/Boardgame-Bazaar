from django.shortcuts import render, get_object_or_404
from .models import Product


def product_detail(request, product_id):
    """
    View to show individual product details
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
