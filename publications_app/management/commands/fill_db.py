from django.core.management import BaseCommand
from publications_app.models import Author, Article, Commentary
from random import randint


class Command(BaseCommand):
    help = "Fill DB with fake data"

    def handle(self, *args, **kwargs):
        for i in range(10):
            author = Author(
                first_name=f"Author{i}",
                last_name=f"McAuthor{i}",
                email=f"author{i}@email.com",
                bio=f"bio{i}",
                birthday=f"{1990 + randint(0, 23)}-{randint(1, 12):02d}-{1 + i:02d}"
            )
            author.save()
        for i in range(30):
            article = Article(
                title=f"Title{i}",
                text=f"Some text{i}",
                publication_date=f"2023-{randint(1, 8):02d}-{1 + i:02d}",
                cathegory=f"Category{randint(0, 4)}",
                author=Author.objects.filter(first_name=f"Author{randint(0, 9)}").first()
            )
            article.save()
        for i in range(100):
            comment = Commentary(
                author=Author.objects.filter(first_name=f"Author{randint(0, 9)}").first(),
                article=Article.objects.filter(title=f"Title{randint(0, 29)}").first(),
                commentary=["Great!", "Awful!"][randint(0,1)],
                created="2023-09-03",
                edited=["2023-09-03", "2023-09-04"][randint(0,1)]
            )
            comment.save()


