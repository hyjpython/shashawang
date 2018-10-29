from django.db import models

# Create your models here.
class Wheel(models.Model):
    w_img = models.CharField(max_length=255)

class FlashSale(models.Model):
    count = models.CharField(max_length=20)
    pic = models.CharField(max_length=256)
    buyNum = models.IntegerField()
    price = models.FloatField()
    dis = models.CharField(max_length=100)
    des01 = models.CharField(max_length=256)
    des02 = models.CharField(max_length=256)
    des03 = models.CharField(max_length=256)
    des04 = models.CharField(max_length=100)