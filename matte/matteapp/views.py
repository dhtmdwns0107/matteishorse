from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Result

def index(request):
    question_list = Question.objects.filter(test_id = 1)
    return render(request, 'matteapp/index.html', {'question_list' : question_list})


def index2(request):
    return render(request, 'matteapp/index2.html', {})

def signin(request):
    return render(request, 'matteapp/signin.html', {})
def signup(request):
    return render(request, 'matteapp/signup.html', {})

def test1(request):
    test_id = request.GET.get('test_id')
    question_list = Question.objects.filter(test_id = test_id)
    return render(request, 'matteapp/test1.html', {'question_list' : question_list})

def result(request):
    test_id = request.GET.get('test_id')
    num = request.POST.get('total')
    print(num)
    result_list = Result.objects.filter(test_id = test_id)
    
    for result in result_list:
        selected_id = result.res_id
        if result.res_div >= int(num):
            break

    print(selected_id)
    return render(request, 'matteapp/result.html', {'result_list' : result_list, 'selected_id' : selected_id})
