from django.core.management.base import BaseCommand
from hometask_app.models import Client    
    
class Command(BaseCommand):
    help = "Add test clients."
        
    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com',phone=79153335555,address='MoscowCity 1')
        client.save()
        client = Client(name='Mike', email='mike@example.com',phone=79153335556,address='MoscowCity 2')
        client.save()
        client = Client(name='Frank', email='frank@example.com',phone=79153335557,address='MoscowCity 3')
        client.save()
        client = Client(name='Paul', email='paul@example.com',phone=79153335558,address='MoscowCity 4')
        client.save()
        client = Client(name='Jack', email='jack@example.com',phone=79153335559,address='MoscowCity 5')
        client.save()
        