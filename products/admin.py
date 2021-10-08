from django.contrib import admin
from .models import Product, Genre, GenreAssignment, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'stock',
        'sold',
        'release_date',
        'image',
        'rating',
    )

    ordering = ('sku',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'rating',
        'user',
        'created',
    )

    ordering = ('created',)


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class GenreAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'genre',
    )

    ordering = ('product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(GenreAssignment, GenreAssignmentAdmin)
admin.site.register(Review, ReviewAdmin)
