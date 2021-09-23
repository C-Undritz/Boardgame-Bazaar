from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update_stock/<int:product_id>/', views.update_stock, name='update_stock'),
    path('review_rate/<order_ref>/<int:product_id>/', views.review_rate, name='review_rate'),
]
