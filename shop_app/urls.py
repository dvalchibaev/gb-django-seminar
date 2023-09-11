from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("clients/", views.clients, name="clients"),
    path("orders/", views.orders, name="orders"),
    path("items/", views.items, name="items"),
    path("client_orders/<int:client_id>/", views.ClientOrders.as_view(), name="client_orders"),
    path("client_orders/<int:client_id>/<str:date_range>/", views.ClientOrders.as_view(), name="client_orders"),
    path("create_orders/<str:date>/", views.create_fake_orders, name="create_fake_orders"),
]
