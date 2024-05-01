from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_brand, name='add_brand'),
]