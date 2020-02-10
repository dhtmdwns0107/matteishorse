from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Qresult, Profile, Choice, Mindtest, Mypage
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
    user = User.objects.get(username = request.user.username)
    user_id = user.id
    mindtest_list = Mindtest.objects.all()
    mypage_list = Mypage.objects.filter(user_id = user_id)
    myresult_list = Qresult.objects.all()
    
    return render(request, 'matteapp/mypage.html', {'mypage_list': mypage_list, 'myresult_list': myresult_list, 'mindtest_list' : mindtest_list})

def test1(request):
    test_id = request.GET.get('test_id')
    question_list = Question.objects.filter(test_id = test_id)
    return render(request, 'matteapp/test1.html', {'question_list' : question_list})

def update(request):
    user = User.objects.get(username = request.user.username)
    if request.method == 'POST':
        #id = request.user.id
        #user = User.objects.get(pk=id)
        update_name = request.POST.get('username')
        if update_name:
            user.username = update_name
        
        update_email = request.POST.get('email')
        if update_email:
            user.email = update_email
        user.save()
        # return redirect('/')
    return render(request, 'matteapp/update.html', {'username':user.username, 'email':user.email})

def result(request):
    test_id = request.POST.get('test_id')
    num = request.POST.get('total')
    result_list = Qresult.objects.filter(test_id = test_id)
    
    selected_id = 1
    for result in result_list:
        if result.res_div > int(num):
            break
        selected_id = result.res_id
        selected_video = result.res_videolink

    choice = Choice(
        c_val = num,
        c_date = timezone.now(),
        q_id = test_id,
        user_id = request.user.id
    )
    choice.save()

    # sum_list = [ ~10��, 20��, 30��, 40��, 50��, 60��~ ]
    choice_list = Choice.objects.filter(q_id = test_id)
    age_list_10 = []
    age_list_20 = []
    age_list_30 = []
    age_list_40 = []
    age_list_50 = []
    age_list_60 = []

    for choice in choice_list:
        age_val = Profile.objects.filter(user_id = choice.user_id)[0].age
        #print("c_id:", choice.c_id, "val:", choice.c_val, "q_id:", choice.q_id, "user:", choice.user_id, "age:", age_val)
        if age_val // 10 == 0:
            age_list_10.append(choice.c_val)
        elif age_val // 10 == 1:
            age_list_10.append(choice.c_val)
        elif age_val // 10 == 2:
            age_list_20.append(choice.c_val)
        elif age_val // 10 == 3:
            age_list_30.append(choice.c_val)
        elif age_val // 10 == 4:
            age_list_40.append(choice.c_val)
        elif age_val // 10 == 5:
            age_list_50.append(choice.c_val)
        else:
            age_list_60.append(choice.c_val)
        
    sum_list = []
    if sum(age_list_10) != 0: sum_list.append(sum(age_list_10)//len(age_list_10))
    else:                     sum_list.append(0)
    if sum(age_list_20) != 0: sum_list.append(sum(age_list_20)//len(age_list_20))
    else:                     sum_list.append(0)
    if sum(age_list_30) != 0: sum_list.append(sum(age_list_30)//len(age_list_30))
    else:                     sum_list.append(0)
    if sum(age_list_40) != 0: sum_list.append(sum(age_list_40)//len(age_list_40))
    else:                     sum_list.append(0)
    if sum(age_list_50) != 0: sum_list.append(sum(age_list_50)//len(age_list_50))
    else:                     sum_list.append(0)
    if sum(age_list_60) != 0: sum_list.append(sum(age_list_60)//len(age_list_60))
    else:                     sum_list.append(0)

    max_score = Mindtest.objects.get(pk=test_id).test_maxscore

    mypage = Mypage(
        test_date = timezone.now(),
        test_id = test_id,
        user_id = request.user.id,
        res_id = selected_id
    )
    mypage.save()
    
    return render(request, 'matteapp/result.html', {'result_list' : result_list, 'selected_id' : selected_id, 'sum_list' : sum_list, 'max_score' : max_score, "num" : num, "selected_video" : selected_video})
