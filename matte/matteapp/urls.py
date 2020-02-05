
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('test1/', views.test1, name='test1'),
]
