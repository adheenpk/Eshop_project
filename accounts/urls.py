
from django.urls import path, include
from . import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')

  ]