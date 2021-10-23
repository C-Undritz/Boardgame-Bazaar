"""
Boardgame Bazaar: home App - Urls
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('shipping/', views.shipping, name='shipping'),
    path('returns/', views.returns, name='returns'),
    path('tandcs/', views.tandcs, name='tandcs'),
    path('careers/', views.careers, name='careers'),
    path('privacy/', views.privacy, name='privacy'),
]
