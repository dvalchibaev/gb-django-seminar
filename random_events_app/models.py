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


class Dice_d6(Model):
    roll = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    objects = Manager

    def __str__(self):
        return f"{self.roll} {self.time}"

    @staticmethod
    def last_rolls(n: int = 1):
        result = Dice_d6.objects.all()
        return result[len(result)-n:]


class Random100(Model):
    number = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    objects = Manager

    def __str__(self):
        return f"{self.number} {self.time}"

    @staticmethod
    def last_rolls(n: int = 1):
        result = Random100.objects.all()
        return result[len(result) - n:]