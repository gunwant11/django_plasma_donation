from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("donate", views.donate, name='donate'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("login", views.loginPage, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("signup", views.signup, name='signup'), 
]
