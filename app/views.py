from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Wheel, FlashSale, NewArrivals


def hello(request):
    return HttpResponse('hello')

# 首页
def index(request):
    wheels = Wheel.objects.all()
    flashsales = FlashSale.objects.all()
    newarrivals = NewArrivals.objects.all()
    response_data = {
        'wheels' : wheels,
        'flashsales':flashsales,
        'newarrivals':newarrivals
    }
    return render(request,'index.html',context=response_data)
