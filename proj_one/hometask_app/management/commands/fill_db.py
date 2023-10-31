from django.core.management.base import BaseCommand
from hometask_app.models import Order, Client, GoodOne
from random import randint, sample
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "Add test db."
        
    def handle(self, *args, **kwargs):
        for i in range (1,101):
           good = GoodOne(name=f'stuff{i}', descr=f'{100-i}everything good',price=i+(100-i)/100,count=randint(10,20),date_added=datetime.now()-timedelta(days=i))
           good.save()
        for i in range (1,101):
            client = Client(name=f'User{i}', email=f'User{i}@example.com',phone=79153335500+i,address=f'MoscowCity{i}',date_reg=datetime.now()-timedelta(days=366+i))
            client.save()
            for j in range (1,366):
                if randint(1,20) == 1:
                    order = Order(customer=client,date_order=datetime.now()-timedelta(days=1+j))
                    order.save()
                    list_goods_id = sample(range(1,101),randint(1,5))
                    for good_id in list_goods_id:
                        order.goods.add(GoodOne.objects.filter(pk=good_id).first())
                    order.save()