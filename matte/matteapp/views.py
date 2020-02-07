from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Qresult, Profile, Choice
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.utils import timezone

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
            email = request.POST['useremail']
        )
        auth.login(request, user)
        profile = Profile(
            gender = request.POST['usersex'],
            age = request.POST['userage'],
            addr = request.POST['useraddr'],
            user_id = request.user.id
        )
        profile.save()

    return render(request, 'matteapp/signup.html', {})

def signout(request):
    logout(request)
    return render(request, 'matteapp/index.html', {})

def mypage(request):
    return render(request, 'matteapp/mypage.html', {})

def test1(request):
    test_id = request.GET.get('test_id')
    question_list = Question.objects.filter(test_id = test_id)
    return render(request, 'matteapp/test1.html', {'question_list' : question_list})

def update(request):
    user = User.objects.get(username = request.user.username)
    if request.method == 'POST':
        #id = request.user.id
        #user = User.objects.get(pk=id)
        user.username = request.POST.get('username')
        user.save()
        # return redirect('/')
    return render(request, 'matteapp/update.html', {'username':user.username})

def result(request):
    test_id = request.POST.get('test_id')
    num = request.POST.get('total')
    result_list = Qresult.objects.filter(test_id = test_id)
    
    selected_id = 1
    for result in result_list:
        if result.res_div > int(num):
            break
        selected_id = result.res_id

    choice = Choice(
        c_val = num,
        c_date = timezone.now(),
        q_id = test_id,
        user_id = request.user.id
    )
    choice.save()

    return render(request, 'matteapp/result.html', {'result_list' : result_list, 'selected_id' : selected_id})
