"""
Boardgame Bazaar: cart App - cart_tools
"""


from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculates the subtotal to be displayed in the cart and checkout pages.
    """
    return price * quantity
