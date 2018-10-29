from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Wheel


def hello(request):
    return HttpResponse('hello')

# 首页
def index(request):
    wheels = Wheel.objects.all()
    response_data = {
        'wheels' : wheels
    }
    return render(request,'index.html',context=response_data)
