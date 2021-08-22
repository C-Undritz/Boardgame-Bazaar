from django.contrib import admin
from .models import Product, Genre, Status, Condition, GenreAssignment

# Register your models here.
admin.site.register(Product)
admin.site.register(Genre)
admin.site.register(Status)
admin.site.register(Condition)
admin.site.register(GenreAssignment)
