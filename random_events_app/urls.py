from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("tosses/", views.get_last_tosses, name="last_tosses"),
    path("<str:game_name>/<int:games>/", views.GameView.as_view(), name="games"),
    path("<str:game_name>/", views.GameView.as_view(), name="game"),
]