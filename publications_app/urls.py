from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.authors, name="authors"),
    path("articles/", views.articles, name="articles"),
    path("create_authors/", views.generate_authors, name="create_authors"),
    path("create_articles/", views.generate_article, name="create_articles"),
]
