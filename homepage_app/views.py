import logging

from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    try:
        with open("./homepage_app/static/index.html", "r") as page:
            html_response = page.read()
    except Exception as e:
        logger.exception(f'Error in home page: {e}')
        return HttpResponse("500 Internal server error")
    else:
        logger.info("Home page accessed")
        return HttpResponse(html_response)


def about(request):
    try:
        with open("./homepage_app/static/about.html", "r") as page:
            html_response = page.read()
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("500 Internal server error")
    else:
        logger.info("About page accessed")
        return HttpResponse(html_response)
