import logging

from django.shortcuts import render
from django.http import HttpResponse

from random import choice, randint


logger = logging.getLogger(__name__)


def heads_or_tails(request):
    logger.debug("heads_or_tails request")
    result = choice(["HEADS", "TAILS"])
    logger.info(f"{result=}")
    return HttpResponse(result)


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
