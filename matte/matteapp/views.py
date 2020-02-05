from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'matteapp/index.html', {})


def index2(request):
    return render(request, 'matteapp/index2.html', {})
