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
    responseData = {
        'msg': '',
        'status': ''
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            # 密码错误
            if user.password != password:
                responseData['msg'] = '密码错误'
                responseData['status'] = '-1'
                return JsonResponse(responseData)
            # 密码正确
            else:
                user.token = str(uuid.uuid5(uuid.uuid4(),'login'))
                user.save()
                request.session['token'] = user.token
                responseData['msg'] = '登录成功'
                responseData['status'] = '1'
                return JsonResponse(responseData)
        # 账号错误
        except:
            responseData['msg'] = '账号不存在'
            responseData['status'] = '-2'
            return JsonResponse(responseData)
    elif request.method == 'GET':
        responseData['msg'] = '请求方式错误'
        responseData['status'] = '2'
        return JsonResponse(responseData)




def cart(request):
    return render(request,'Shopping Cart.html')


def quit(request):
    logout(request)
    return redirect('app:index')