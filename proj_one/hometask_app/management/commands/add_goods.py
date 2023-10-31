from django.core.management.base import BaseCommand
from hometask_app.models import GoodOne
    
class Command(BaseCommand):
    help = "Add test goods."
        
    def handle(self, *args, **kwargs):
        good = GoodOne(name='stuff', descr='everything good',price=223.44,count=11)
        good.save()
        good = GoodOne(name='prize', descr='everything good',price=224.44,count=12)
        good.save()
        good = GoodOne(name='furniture', descr='everything good',price=225.44,count=13)
        good.save()
        good = GoodOne(name='hardware', descr='everything good',price=226.44,count=14)
        good.save()
        good = GoodOne(name='software', descr='everything good',price=227.44,count=15)
        good.save()
        