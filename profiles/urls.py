from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('address/', views.profile_address, name='profile_address'),
    path('order_history/', views.profile_orders, name='profile_orders'),
    path('order_detail/<order_number>/', views.order_detail, name='order_detail'),
    path('wishlist_toggle/<product_id>/<int:nav>/', views.wishlist_toggle, name='wishlist_toggle'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('mailinglist/', views.profile_mailinglist, name='profile_mailinglist')
]
