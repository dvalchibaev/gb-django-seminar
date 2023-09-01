import logging

from django.shortcuts import render
from django.http import HttpResponse

from random import choice, randint

from . import models


logger = logging.getLogger(__name__)


def heads_or_tails(request):
    logger.debug("heads_or_tails request")
    result = choice(["HEADS", "TAILS"])
    cointoss = models.Cointoss(toss=result)
    cointoss.save()
    logger.info(f"{cointoss=}")
    return HttpResponse(f"{cointoss}")


def get_last_tosses(request):
    return HttpResponse([str(toss) + '<br>' for toss in models.Cointoss.last_tosses(10)])


def roll_d6(request):
    logger.debug("roll_d6 request")
    result = randint(1, 6)
    logger.info(f"{result=}")
    return HttpResponse(str(result))


def random100(request):
    logger.debug("heads_or_tails request")
    result = randint(0, 100)
    logger.info(f"{result=}")
    return HttpResponse(str(result))
