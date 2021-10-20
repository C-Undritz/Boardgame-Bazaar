"""
Boardgame Bazaar: home App - Urls
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('information/', views.information, name='information'),
]
