from django.http import HttpResponse
from . import models


def clients(request):
    result = "<br>".join(str(client) for client in models.Client.objects.all())
    return HttpResponse(result)


def orders(request):
    result = "<br>".join(str(order) for order in models.Order.objects.all())
    return HttpResponse(result)


def items(request):
    result = "<br>".join(str(item) for item in models.Item.objects.all())
    return HttpResponse(result)



