from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    return render(request, 'matteapp/index.html', {})


def index2(request):
    return render(request, 'matteapp/index2.html', {})

def test1(request):
    question_list = Question.objects.filter(test_id = 1)
    return render(request, 'matteapp/test1.html', {'question_list' : question_list})
