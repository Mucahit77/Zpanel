from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#http://127.0.0.1:8000/user

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
