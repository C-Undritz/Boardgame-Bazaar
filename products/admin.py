from django.contrib import admin
from .models import Product, Genre, Category, Condition, GenreAssignment

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
    )

    ordering = ('sku',)


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
