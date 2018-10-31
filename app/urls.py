from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^hello/$',views.hello),
    url(r'^$',views.index,name='index'),
    url(r'^register$',views.register,name='register'),
    url(r'^login$',views.login,name='login'),
    url(r'^cart$',views.cart,name='cart')

]