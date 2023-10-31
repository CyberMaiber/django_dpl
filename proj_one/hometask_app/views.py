# from django.shortcuts import render
# from http import client
import logging
from django.http import HttpResponse
from django.shortcuts import render #get_object_or_404
from .models import Client, Order, GoodOne
from datetime import datetime, timedelta
from .forms import AddImageToGoodForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage


logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed.')
    return render(request,'hometask_app/base.html')

def orders_of_client(request,client_id,days_count):
    logger.info('Orders page accessed.')
    client = Client.objects.filter(pk=client_id)
    orders = Order.objects.filter(customer=client_id)\
                          .filter(date_order__date__gt=datetime.now()-timedelta(days=days_count))\
                          .order_by('date_order')
    goods_of_client = []
    for order in orders:
        for good in order.goods.filter():
            if not good in goods_of_client:
                goods_of_client.append(good)
    
    # context = {'goods':goods_of_client, 'client': client, 'lst_days':days_count}
    return render(request,'hometask_app/ordrs_clnt.html', {'goods':goods_of_client, 'client': client, 'lst_days':days_count})

def all_goods_list(request):
    logger.info('all_goods_list page accessed.')
    goods = GoodOne.objects.all()
    return render(request,'hometask_app/all_goods.html',{'goods':goods})

def good_add_image(request,good_id):
    good = GoodOne.objects.filter(pk=good_id).first()
    fs = FileSystemStorage(location=f'{settings.STATIC_APP}/media/hometask_app/')
    
    if request.method == 'POST':
        form = AddImageToGoodForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            image = form.cleaned_data['image']
            fs.save(f'image{good.pk}',image)
            good.image_file = f'image{good.pk}'
            print (f'image{good.pk}')
            good.save()
    else:
        form = AddImageToGoodForm()
    return render(request,'hometask_app/good_edit.html',{'form':form, 'good':good})

def about(request):
    logger.info('About page accessed.',{})
    html = ("<h1>О себе</h1>\n"+
            "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel, veniam?</p>\n"+
            "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel, veniam?</p>\n"+
            "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel, veniam?</p>\n"+
            "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel, veniam?</p>\n"+
            "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel, veniam?</p>\n"
            )

    return HttpResponse(html)


