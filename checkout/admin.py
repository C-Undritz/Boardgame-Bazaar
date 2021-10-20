"""
Boardgame Bazaar: checkout App - Admin
"""


from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Display for orderlineitem model fields in admin
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Adds the inlines option (from above) in the order admin class and sets
    out the database fields visible in admin.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name', 'email',
              'phone_number', 'country', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'postcode', 'discount',
              'delivery_cost', 'order_total', 'grand_total', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name', 'grand_total',)

    # ordered by reverse date order; most recent orders at the top.
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
