from django.db import models

# Create your models here.
class Wheel(models.Model):
    w_img = models.CharField(max_length=255)

class FlashSale(models.Model):
    count = models.CharField(max_length=20)
    pic = models.CharField(max_length=256)
    buyNum = models.IntegerField()
    price = models.CharField(max_length=50)
    dis = models.CharField(max_length=100)
    des01 = models.CharField(max_length=256)
    des02 = models.CharField(max_length=256)
    des03 = models.CharField(max_length=256)
    des04 = models.CharField(max_length=100)

class NewArrivals(models.Model):
    messpic = models.CharField(max_length=20)
    coupic = models.CharField(max_length=20)
    pic = models.CharField(max_length=256)
    saleNum = models.CharField(max_length=20,default='')
    price = models.CharField(max_length=20)
    dis = models.CharField(max_length=20)
    count = models.CharField(max_length=20)
    des02 = models.CharField(max_length=50)
    des03 = models.CharField(max_length=100)
    des04 = models.CharField(max_length=20)
    des05 = models.CharField(max_length=256)

class HotBrand(models.Model):
    img = models.CharField(max_length=256)
    logo = models.CharField(max_length=256)

class User(models.Model):
    username = models.CharField(max_length=256,unique=True)
    password = models.CharField(max_length=256)
    token = models.CharField(max_length=256)