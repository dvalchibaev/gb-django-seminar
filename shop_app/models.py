from django.db import models
from django.core.validators import MinValueValidator


class Client(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateField()

    def __str__(self):
        return f"{self.name}, {self.email}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total_sum = models.DecimalField(max_digits=12, decimal_places=2,
                                    validators=[MinValueValidator(0.0)])
    date = models.DateField()

    def __str__(self):
        return f"Total sum: {self.total_sum}, date of order: {self.date}"


class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.0)])
    amount = models.PositiveIntegerField()
    date_added = models.DateField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    image = models.ImageField(default="stock_item.jpg")

    def __str__(self):
        return f"Item: {self.name}, price {self.price}, #: {self.amount}"
