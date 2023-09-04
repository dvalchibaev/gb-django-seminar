import logging

from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    template = "homepage_app/index.html"
    return render(request, template)


def about(request):
    template = "homepage_app/about.html"
    return render(request, template)
