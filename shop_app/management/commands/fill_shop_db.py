from django.core.management import BaseCommand
from shop_app import models
from random import randint, choice


def update_order_price(ord: models.Order):
    items = models.Item.objects.filter(order=ord)
    ord.total_sum = sum([item.price * item.amount for item in items])
    ord.save()


class Command(BaseCommand):
    help = "Fill DB with fake data"

    def handle(self, *args, **kwargs):
        ITEMS = [(f"item_{i}", randint(100, 50_000)) for i in range(100)]

        for i in range(10):
            client = models.Client(
                name=f"Client_{i}",
                email=f"client{i}@email.com",
                phone=f"+7(999)99-99-9{i:02d}",
                address="random_address",
                registration_date= f"2023-08-{1+i:02d}"
            )
            client.save()
            for j in range(randint(1,3)):
                order = models.Order(
                    client=client,
                    total_sum=0.0,
                    date=f"2023-09-{2+j:02d}",
                )
                order.save()
                for _ in range(randint(2,10)):
                    name_price = choice(ITEMS)
                    item = models.Item(
                        name=name_price[0],
                        description="description",
                        price=name_price[1],
                        amount=randint(1,5),
                        date_added=f"2023-09-{2+j:02d}",
                        order=order
                    )
                    item.save()
                update_order_price(order)
                order.save()


