from django.http import HttpResponse
from .models import Author, Article
from random import randint


def authors(request):
    return HttpResponse("Authors dummy")


def articles(request):
    return HttpResponse("Articles dummy")


def generate_authors(request):
    for i in range(10):
        author = Author(
            first_name=f"Author{i}",
            last_name=f"McAuthor{i}",
            email=f"author{i}@email.com",
            bio=f"bio{i}",
            birthday=f"{1990+randint(0,23)}-{randint(1,12):02d}-{1+i:02d}"
            )
        author.save()
    return HttpResponse("OK")


def generate_article(request):
    for i in range(30):
        article = Article(
            title=f"Title{i}",
            text=f"Some text{i}",
            publication_date=f"2023-{randint(1,8):02d}-{1+i:02d}",
            cathegory=f"Category{randint(0,4)}",
            author=Author.objects.filter(pk=randint(1,10)).first()
            )
        article.save()
    return HttpResponse("OK")

