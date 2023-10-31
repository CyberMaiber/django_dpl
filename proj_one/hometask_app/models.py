from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=100) #имя клиента
    email = models.EmailField(unique=True) #почта клиента
    phone = models.CharField(max_length=12)#телефон клиента
    address = models.TextField()#адрес клиента
    date_reg = models.DateField(default=timezone.now)#дата регистрации клиента

    def __str__(self) -> str:
        return f'Client|ID:{self.pk}, Name:{self.name}, Email:{self.email}, Phone:{self.phone}, Date_reg:{self.date_reg}'


class GoodOne(models.Model):
    name = models.CharField(max_length=100) #имя товара
    descr = models.TextField()#описание товара
    price = models.DecimalField(max_digits=12,decimal_places=2) #цена товара
    count = models.IntegerField()#количество товара
    date_added = models.DateField(default=timezone.now)#дата поступления товара
    image_file = models.CharField(max_length=100, default='noimage.png') #имя файла с изображением товара

    def __str__(self) -> str:
        return f'Good|ID:{self.pk}, Name:{self.name}, Descr:{self.descr}, price:{self.price}, count:{self.count}, date_added:{self.date_added}, image_file:{self.image_file}'

class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE) # покупатель (ссылка на покупателя)
    goods = models.ManyToManyField(GoodOne)#перечень товаров в заказе(ссылки на товары)
    # total_price = models.DecimalField(max_digits=12,decimal_places=2) #сумма заказа 
    date_order = models.DateTimeField(default=timezone.now)#дата заказа

    @property
    def total_price (self):
        result = 0
        for good in self.goods.filter():
            result += good.price
        return result

    def __str__(self) -> str:
        goods_list = []
        for good in self.goods.filter():
            goods_list.append(str(good))
        nl = '\n'
        return f'Order ID:{self.pk}|\ncustomer:{self.customer}\ngoods:\n{nl.join(goods_list)}\ntotal_price:{self.total_price}\ndate_order:{self.date_order}'
