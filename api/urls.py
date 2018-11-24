from django.urls import path

from . import views

urlpatterns = [
    path('deposits', views.deposits, name='deposits'),
    path('promotions', views.promotions, name='promotions'),
]