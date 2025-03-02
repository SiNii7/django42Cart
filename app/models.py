from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Tovar(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    image = models.FileField(verbose_name='Изображение', upload_to='img/', null=True, blank=True)
    discount = models.IntegerField(verbose_name='Скидка', null=True, blank=True, default=0)
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    tovar = models.ForeignKey(to=Tovar, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Количество', default=1)
    summa = models.DecimalField(max_digits=12,decimal_places=2,verbose_name='Сумма')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def calcSumma(self):
        return self.count*(self.tovar.price - self.tovar.price*self.tovar.discount/100)

class Status(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    adress = models.CharField(verbose_name='Адрес', max_length=1000)
    email = models.EmailField(verbose_name='Email')
    tel = models.CharField(verbose_name='Телефон', max_length=20)
    tovars = models.ManyToManyField(to=Tovar)
    status = models.ForeignKey(to=Status, on_delete=models.SET_NULL, null=True, blank=True,verbose_name='Статус')
    total = models.DecimalField(max_digits=12,decimal_places=2,verbose_name='Итог')
    data = models.DateTimeField(auto_created=True, verbose_name='Дата',null=True, blank=True)
    zakaz = models.TextField(verbose_name='Заказ')

    def __str__(self):
        return f'{self.data} --- {self.adress}'