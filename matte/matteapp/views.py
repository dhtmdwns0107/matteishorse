from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Result

def index(request):
    return render(request, 'matteapp/index.html', {})


def index2(request):
    return render(request, 'matteapp/index2.html', {})

def signin(request):
    return render(request, 'matteapp/signin.html', {})
def signup(request):
    return render(request, 'matteapp/signup.html', {})

def test1(request):
    question_list = Question.objects.filter(test_id = 1)
    return render(request, 'matteapp/test1.html', {'question_list' : question_list})

def result(request): # 투표 결과 페이지
    num = request.POST.get('total')
    print(num)
    # question = Question.objects.get(pk=q_id) # models.py에서 이거 자체가 객체로 지정되어 있기 때문에
    # choices = question.choice_set.all()
    # choices = Choice.objects.filter(question=question) # 이건 뭔 방식이지 근데 위와 같은 방식이라고 한다
    result_list = Result.objects.filter(test_id = 1)
    
    for result in result_list:
        selected_id = result.res_id
        if result.res_div >= int(num):
            break

    print(selected_id)
    return render(request, 'matteapp/result.html', {'result_list' : result_list, 'selected_id' : selected_id})
