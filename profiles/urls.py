from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/', views.profile_orders, name='profile_orders'),
    path('order_detail/<order_number>', views.order_detail, name='order_detail'),
]
