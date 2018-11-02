import uuid

from django.contrib.auth import logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Wheel, FlashSale, NewArrivals, HotBrand, User

def hello(request):
    return HttpResponse('hello')

# 首页
def index(request):
    wheels = Wheel.objects.all()
    flashsales = FlashSale.objects.all()
    newarrivals = NewArrivals.objects.all()
    hotbrands = HotBrand.objects.all()
    token = request.session.get('token')
    response_data = {
        'wheels': wheels,
        'flashsales': flashsales,
        'newarrivals': newarrivals,
        'hotbrands': hotbrands,
    }
    if token:
        user = User.objects.get(token=token)
        response_data['username'] = user.username
        return render(request,'index.html',context=response_data)
    else:
        return render(request,'index.html',context=response_data)


def register(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.token = str(uuid.uuid5(uuid.uuid4(),'register'))
        user.save()

        request.session['token'] = user.token

        return redirect('app:index')
    elif request.method == 'GET':
        return render(request,'register.html')




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            # 密码错误
            if user.password != password:
                return render(request,'login.html',context={'defeat':'账号或密码错误'})
            # 密码正确
            else:
                user.token = str(uuid.uuid5(uuid.uuid4(),'login'))
                user.save()
                request.session['token'] = user.token
                return redirect('app:index')
        # 账号错误
        except:
            return render(request,'login.html',context={'defeat':'用户不存在'})
    elif request.method == 'GET':
       return render(request,'login.html')




def cart(request):
    return render(request,'Shopping Cart.html')


def quit(request):
    logout(request)
    return redirect('app:index')


def detail(request,page):
    newarrivals = NewArrivals.objects.all()[int(page)-1]



    return render(request,'Product Details.html',context={'newarrivals':newarrivals})