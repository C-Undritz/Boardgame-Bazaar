from django.contrib import admin
from .models import Product, Genre, Status, Condition, GenreAssignment

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'product_name',
        'status',
        'condition',
        'price',
        'stock',
        'status',
        'image',
    )

    ordering = ('sku',)


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class StatusAdmin(admin.ModelAdmin):
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
        'Product',
        'genre',
    )

    ordering = ('Product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(GenreAssignment, GenreAssignmentAdmin)
