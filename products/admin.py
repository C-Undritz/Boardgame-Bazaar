from django.contrib import admin
from .models import Product, Genre, Category, Condition, GenreAssignment, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'product_name',
        'condition',
        'price',
        'stock',
        'category',
        'release_date',
        'image',
        'avg_rating',
    )

    ordering = ('sku',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'review',
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


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ConditionAdmin(admin.ModelAdmin):
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
admin.site.register(Category, CategoryAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(GenreAssignment, GenreAssignmentAdmin)
admin.site.register(Review, ReviewAdmin)
