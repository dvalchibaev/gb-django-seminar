from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Author, Article, Commentary
from random import randint, choice


class PubView(TemplateView):
    template_name = "publications_app/publications_by_author.html"

    def get_context_data(self, author_id: int, **kwargs):
        context =super().get_context_data(**kwargs)
        author = get_object_or_404(Author, pk=author_id)
        articles = Article.objects.filter(author=author)
        context['author_name'] = str(author)
        context['articles'] = articles
        return context


def authors(request):
    authors = Author.objects.all()
    result = '<br>'.join([str(author) for author in authors])
    return HttpResponse(result)


def articles(request):
    arts = Article.objects.all()
    result = ''
    for art in arts:
        result += f"{art.title} by {art.author}, {art.publication_date}<br>"
    return HttpResponse(result)


def comments(request):
    commentaries = Commentary.objects.all()
    result = ''
    for com in commentaries:
        result += f"{com.author} on {com.article.title}, {com.created}: {com.commentary} <br>"
    return HttpResponse(result)


# def get_authors_articles(request, pk):
#     arts = Article.objects.filter(pk=pk).all()
#     return arts