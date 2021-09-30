from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('add_genre/', views.add_genre, name='add_genre'),
    path('edit/<int:product_id>/<int:nav>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/<int:nav>/', views.delete_product, name='delete_product'),
    path('products_list/', views.products_list, name='products_list'),
    path('update_stock/<int:product_id>/', views.update_stock, name='update_stock'),
    path('review_rate/<order_number>/<int:product_id>/', views.review_rate, name='review_rate'),
]
