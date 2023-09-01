from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("heads_or_tails/", views.heads_or_tails, name="toss_a_coin"),
    path("roll_d6/", views.roll_d6, name="roll_d6"),
    path("random_100/", views.random100, name="random_100"),
    path("tosses/", views.get_last_tosses, name="last_tosses"),
]
