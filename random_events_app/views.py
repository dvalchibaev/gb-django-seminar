import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from random import choice, randint

from . import models


logger = logging.getLogger(__name__)


class GameView(TemplateView):
    template_name = "random_events_app/game.html"

    def get_context_data(self, game_name: str, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game_title'] = game_name
        result = []
        games = kwargs.get('games') if kwargs.get('games') else 1
        for _ in range(games):
            match game_name.lower():
                case "heads_or_tails":
                    result.append("result: " + self.play_heads_or_tails())
                case "roll_d6":
                    result.append("result: " + self.play_d6())
                case "random100":
                    result.append("result: " + self.play_random100())
        context["rolls"] = result
        return context

    def play_heads_or_tails(self):
        result = choice(("heads", "tails"))
        toss = models.Cointoss(toss=result)
        toss.save()
        return result

    def play_d6(self):
        result = randint(1,6)
        toss = models.Dice_d6(roll=result)
        toss.save()
        return str(result)

    def play_random100(self):
        result = randint(1,100)
        toss = models.Random100(number=result)
        toss.save()
        return str(result)


def get_last_tosses(request):
    return HttpResponse([str(toss) + '<br>' for toss in models.Cointoss.last_tosses(10)])
