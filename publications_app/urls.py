from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.authors, name="authors"),
    path("articles/", views.articles, name="articles"),
    path("comments/", views.comments, name="comments"),
    path("articles_by/<int:author_id>/", views.PubView.as_view(), name="publications_by_author")
]
