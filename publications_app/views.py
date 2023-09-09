from django.http import HttpResponse
from .models import Author, Article, Commentary
from random import randint, choice


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

