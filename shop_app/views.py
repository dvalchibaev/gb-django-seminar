from django.http import HttpResponse
from django.views.generic import TemplateView

from . import models

from datetime import date
from dateutil.relativedelta import relativedelta

def clients(request):
    result = "<br>".join(str(client) for client in models.Client.objects.all())
    return HttpResponse(result)


def orders(request):
    result = "<br>".join(str(order) for order in models.Order.objects.all())
    return HttpResponse(result)


def items(request):
    result = "<br>".join(str(item) for item in models.Item.objects.all())
    return HttpResponse(result)


def create_fake_orders(request, date):
    clients = models.Client.objects.all()
    for client in clients:
        order = models.Order(client=client, total_sum=0, date=date)
        order.save()
        item = models.Item(
            name=f"Item_{client.name}_{date}",
            description="description",
            price=10000,
            amount=1,
            date_added=date,
            order=order
        )
        item.save()
        order.total_sum = item.price
        order.save()
        client.save()
    return HttpResponse("OK")


class ClientOrders(TemplateView):
    template_name = "shop_app/client_orders.html"

    def get_context_data(self, client_id, **kwargs):
        context = super().get_context_data(**kwargs)
        client = models.Client.objects.filter(pk=client_id, ).first()
        client_orders = models.Order.objects.filter(client=client).all()
        date_range = kwargs.get('date_range')
        if date_range:
            match date_range.lower():
                case "week":
                    filter_date = date.today() - relativedelta(days=7)
                case "month":
                    filter_date = date.today() - relativedelta(months=1)
                case "year":
                    filter_date = date.today() - relativedelta(years=1)
                case _:
                    filter_date = date.today() - relativedelta(years=100)
            client_orders = client_orders.filter(date__gte=filter_date)
        client_orders = client_orders.order_by('date')
        order_items = {}
        for order in client_orders:
            order_items[order] = models.Item.objects.filter(order=order).all()
        context['client_name'] = client.name
        context['client_orders'] = client_orders
        context['order_items'] = order_items
        return context
