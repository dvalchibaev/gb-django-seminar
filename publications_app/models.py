from django.db import models
from django.db.models import Manager, Model


class Author(Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Article(Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cathegory = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return ', '.join([f"{i} = {self.__getattribute__(i)}" for i in dir(self) if not i.startswith("__")])


class Commentary(Model):
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               unique=True)
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                unique=True)
    commentary = models.TextField()
    created = models.DateField()
    edited = models.DateField(default=created)
