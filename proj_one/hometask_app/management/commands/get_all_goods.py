from django.core.management.base import BaseCommand
from hometask_app.models import GoodOne    
    
class Command(BaseCommand):
    help = "Get all goods."
        
    def handle(self, *args, **kwargs):
        goods = GoodOne.objects.all()
        for good_one in goods:
            self.stdout.write(f'{good_one}')