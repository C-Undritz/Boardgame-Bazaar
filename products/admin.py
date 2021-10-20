"""
Boardgame Bazaar: products App - Admin
"""


from django.contrib import admin
from .models import Product, Genre, GenreAssignment, Review


class ProductAdmin(admin.ModelAdmin):
    """
    Sets out the database fields from the Product model visible in admin.
    """
    list_display = (
        'id',
        'name',
        'price',
        'stock',
        'sold',
        'release_date',
        'image',
        'rating',
    )

    ordering = ('id',)


class ReviewAdmin(admin.ModelAdmin):
    """
    Sets out the database fields from the Review model visible in admin.
    """
    list_display = (
        'id',
        'product',
        'rating',
        'user',
        'created',
    )

    ordering = ('created',)


class GenreAdmin(admin.ModelAdmin):
    """
    Sets out the database fields from the Genre model visible in admin.
    """
    list_display = (
        'friendly_name',
        'name',
    )


class GenreAssignmentAdmin(admin.ModelAdmin):
    """
    Sets out the database fields from the GenreAssignment model visible in
    admin.
    """
    list_display = (
        'product',
        'genre',
    )

    ordering = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(GenreAssignment, GenreAssignmentAdmin)
admin.site.register(Review, ReviewAdmin)
