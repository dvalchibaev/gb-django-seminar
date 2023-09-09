from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("clients/", views.clients, name="clients"),
    path("orders/", views.orders, name="orders"),
    path("items/", views.items, name="items"),
]
