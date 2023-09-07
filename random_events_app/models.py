from django.db import models
from django.db.models import Manager, Model


class Cointoss(Model):
    toss = models.CharField(max_length=5)
    time = models.DateTimeField(auto_now_add=True)

    objects = Manager

    def __str__(self):
        return f"{self.toss} {self.time}"

    @staticmethod
    def last_tosses(n: int = 1):
        result = Cointoss.objects.all()
        return result[len(result)-n:]
