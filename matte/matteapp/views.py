from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Qresult
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout

def index(request):
    question_list = Question.objects.filter(test_id = 1)
    return render(request, 'matteapp/index.html', {'question_list' : question_list})


def index2(request):
    return render(request, 'matteapp/index2.html', {})

def signin(request):
    if request.method == "POST":
        
        # email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'matteapp/index.html', {})
        else:
            return render(request, 'matteapp/signup.html', {})

def signup(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password'],
            email = request.POST['useremail'],
            # user_age = request.POST['userage'],
            # user_sex = request.POST['usersex'],
            # user_addr = request.POST['useraddr']
        )
        auth.login(request, user)
    return render(request, 'matteapp/signup.html', {})

def signout(request):
    logout(request)
    return render(request, 'matteapp/index.html', {})

def test1(request):
    test_id = request.GET.get('test_id')
    question_list = Question.objects.filter(test_id = test_id)
    return render(request, 'matteapp/test1.html', {'question_list' : question_list})

def result(request):
    test_id = request.GET.get('test_id')
    num = request.POST.get('total')
    print(num)
    result_list = Qresult.objects.filter(test_id = test_id)
    
    for result in result_list:
        selected_id = result.res_id
        if result.res_div >= int(num):
            break

    print(selected_id)
    return render(request, 'matteapp/result.html', {'result_list' : result_list, 'selected_id' : selected_id})
