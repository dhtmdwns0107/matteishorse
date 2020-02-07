
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('test1/', views.test1, name='test1'),
    path('result/', views.result, name='result'),
    path('mypage/', views.mypage, name='mypage'),
    path('update/', views.update, name='update'),
 
]
