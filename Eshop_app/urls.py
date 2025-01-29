from tkinter.font import names

from django.urls import path

from Eshop_app import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('shop/<int:product_id>', views.detail, name='detail'),

    ]