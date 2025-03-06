from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user),
    path('signin_user', views.signin_user),
]
