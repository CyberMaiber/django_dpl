from django.core.management.base import BaseCommand
from hometask_app.models import Order, Client, GoodOne
    
class Command(BaseCommand):
    help = "Add test orders."
        
    def handle(self, *args, **kwargs):
        client = Client.objects.filter(pk=1).first()
        order = Order.objects.create(customer=client)
        order.goods.add(GoodOne.objects.filter(pk=1).first())
        order.goods.add(GoodOne.objects.filter(pk=3).first())
        order.goods.add(GoodOne.objects.filter(pk=2).first())
        self.stdout.write(f'{order}')
        order.save()
     