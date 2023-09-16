from django.contrib import admin
from . import models


class ItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'name', 'price', 'amount', 'date_added']
    ordering = ['order', 'name']
    list_filter = ['order', 'name']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    ordering = ['name']
    list_filter = ['name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_sum', 'date']
    ordering = ['client', 'date']
    list_filter = ['client', 'date']


admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Item, ItemAdmin)
