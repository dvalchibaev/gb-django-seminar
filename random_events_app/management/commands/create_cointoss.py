from django.core.management.base import BaseCommand
from random_events_app.models import Cointoss
from random import choice


class Command(BaseCommand):
    help = "Generate a coin toss: HEADS or TAILS"

    def handle(self, *args, **options):
        result = choice(["HEADS", "TAILS"])
        cointoss = Cointoss(toss=result)
        cointoss.save()
        self.stdout.write(f"{cointoss=}")
