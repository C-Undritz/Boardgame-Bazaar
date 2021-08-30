from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Returns the context dictionary and makes it available to all templates
    across the whole application
    """
    cart_items = []
    total = 0
    product_count = 0
    delivery = 4
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if product_count >= settings.MULTIBUY_DISCOUNT_TWO:
        discount_rate = 5
        discount_amount = Decimal(total * Decimal(settings.MULTIBUY_DISCOUNT_TWO / 100))
        final_total = total - discount_amount
        discount_count_delta = 0
    elif product_count >= settings.MULTIBUY_DISCOUNT_ONE:
        discount_rate = 3
        discount_amount = Decimal(total * Decimal(settings.MULTIBUY_DISCOUNT_ONE / 100))
        final_total = total - discount_amount
        discount_count_delta = settings.MULTIBUY_DISCOUNT_TWO - product_count
    else:
        discount_rate = 0
        discount_amount = 0
        final_total = total
        discount_count_delta = settings.MULTIBUY_DISCOUNT_ONE - product_count


    grand_total = delivery + final_total

    context = {
        'cart_items': cart_items,
        'total': total,
        'final_total': final_total,
        'product_count': product_count,
        'delivery': delivery,
        'discount_count_delta': discount_count_delta,
        'discount_rate': discount_rate,
        'discount_amount': discount_amount,
        'multibuy_discount_one': settings.MULTIBUY_DISCOUNT_ONE,
        'multibuy_discount_two': settings.MULTIBUY_DISCOUNT_TWO,
        'grand_total': grand_total,
    }

    return context
