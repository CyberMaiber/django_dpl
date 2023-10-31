from django.contrib import admin
from .models import Client, GoodOne, Order


# Register your models here.

class ClientAdminView(admin.ModelAdmin):
    list_display = ['name','email','phone']
    search_fields = ['name','email','phone']

class GoodOneAdminView(admin.ModelAdmin):
    list_display = ['name','count','price']
    list_filter = ['name','count']

class OrderAdminView(admin.ModelAdmin):
    list_display = ['pk','customer','total_price','date_order']
    ordering = ['pk']
    readonly_fields = ['customer','total_price']
    fieldsets = [
    (
        None,
        {
            'classes': ['wide'],
            'fields': ['customer'],
        },
    ),
    (
        'Товары',
        {
            'classes': ['collapse'],
            'fields': ['goods'],
        },
    ),
    (
        'Детали',
        {
            'classes': ['collapse'],
            'fields': ['date_order','total_price'],
        }
    ),
    ]


admin.site.register(Client, ClientAdminView)
admin.site.register(GoodOne, GoodOneAdminView)
admin.site.register(Order, OrderAdminView)


