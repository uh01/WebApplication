from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddCarCreateView.as_view(), name='add_car'),
    path('details/<int:id>/', views.DetailCarView.as_view(), name='view_details'),
    path('buy_now/<int:id>/', views.buy_now, name='buy_now'),
]