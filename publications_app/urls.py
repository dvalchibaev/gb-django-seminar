from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.authors, name="authors"),
    path("articles/", views.articles, name="articles"),
    path("comments/", views.comments, name="comments")
]
