"""
Boardgame Bazaar: products App - Urls
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="all_products"),
    path('product_detail/<int:product_id>/',
         views.product_detail,
         name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('products_list/', views.products_list, name='products_list'),
    path('edit/<int:product_id>/<int:nav>/',
         views.edit_product,
         name='edit_product'),
    path('delete/<int:product_id>/<int:nav>/',
         views.delete_product,
         name='delete_product'),
    path('add_genre/', views.add_genre, name='add_genre'),
    path('genres_list/', views.genres_list, name='genres_list'),
    path('edit/<int:genre_id>/', views.edit_genre, name='edit_genre'),
    path('delete/<int:genre_id>/', views.delete_genre, name='delete_genre'),
    path('update_stock/<int:product_id>/',
         views.update_stock,
         name='update_stock'),
    path('review_rate/<order_number>/<int:product_id>/',
         views.review_rate,
         name='review_rate'),
    path('edit_review/<order_number>/<int:product_id>/',
         views.edit_review,
         name='edit_review'),
    path('delete_review/<order_number>/<int:review_id>/',
         views.delete_review,
         name='delete_review'),
]
