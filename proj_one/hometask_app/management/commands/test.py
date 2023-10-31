from django.core.management.base import BaseCommand
from hometask_app.models import Order, Client, GoodOne
from random import randint, sample
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "Add test db."
        
    def handle(self, *args, **kwargs):
        client_id = 6
        days_count = 300
        client = Client.objects.filter(pk=client_id)
        orders = Order.objects.filter(customer=client_id)\
                              .filter(date_order__date__gt=datetime.now()-timedelta(days=days_count))\
                              .order_by('date_order')
        goods_of_client = []
        for order in orders:
            for good in order.goods.filter():
                if not good in goods_of_client:
                    goods_of_client.append(good)
        print(*goods_of_client,sep='\n')