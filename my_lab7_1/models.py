from django.db import models
from django.contrib.auth.models import AbstractUser


class ComputerModel(models.Model):
    id = models.AutoField(primary_key=True)
    serial_num = models.IntegerField(unique=True, verbose_name='Серийный номер')
    #comp_pic = models.ImageField()
    brand = models.CharField(max_length=20, default='Dell')  # производитель
    type = models.CharField(max_length=10, default='laptop')  # desktops, laptop, tablet
    screen_size = models.FloatField(default=11)
    installed_OS = models.CharField(max_length=20, default='Windows8')
    processor_type = models.CharField(max_length=20, default='Inspiron 11')
    RAM = models.FloatField(default=2)
    price = models.CharField(max_length=20, default='30000 руб')
    ord_num = models.ManyToManyField('OrderModel')

    def __str__(self):
        return str(self.serial_num)


class User(AbstractUser):
    phone = models.CharField(max_length=15, default='')
    adress = models.TextField(verbose_name='Адрес', default='')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class OrderModel(models.Model):
    id = models.AutoField(primary_key=True)
    order_num = models.IntegerField(unique=True)
    order_date = models.DateField()
    user_id = models.ForeignKey(User)

    def __str__(self):
        return str(self.order_num)
