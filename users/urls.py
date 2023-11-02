from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView),
    path('signup', views.SignupView),
]