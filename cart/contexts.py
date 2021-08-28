from decimal import Decimal
from django.conf import settings

def cart_contents(request):
    """
    Returns the context dictionary and makes it available to all templates
    across the whole application
    """
    cart_items = []
    total = 0
    product_count = 0
    delivery = 4

    if product_count >= settings.MULTIBUY_DISCOUNT_ONE:
        final_total = total-(total*(settings.MULTIBUY_DISCOUNT_ONE/100))
        discount_count_delta = 0
    else:
        final_total = total
        discount_count_delta = settings.MULTIBUY_DISCOUNT_ONE - product_count

    grand_total = delivery + final_total

    context = {
        'cart_items': cart_items,
        'final_total': final_total,
        'product_count': product_count,
        'delivery': delivery,
        'discount_count_delta': discount_count_delta,
        'multibuy_discount_one': settings.MULTIBUY_DISCOUNT_ONE,
        'grand_total': grand_total,
    }

    return context