from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.user_signin, name='user_signin'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit_profile', views.edit_profile, name='edit_profile'),
    path('profile/pass_change', views.pass_change, name='pass_change'),
    path('logout/', views.user_logout, name='user_logout'),
]