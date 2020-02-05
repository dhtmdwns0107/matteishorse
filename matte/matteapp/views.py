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

def results(request, q_id): # 투표 결과 페이지
    question = Question.objects.get(pk=q_id) # models.py에서 이거 자체가 객체로 지정되어 있기 때문에
    choices = question.choice_set.all()
    choices = Choice.objects.filter(question=question) # 이건 뭔 방식이지 근데 위와 같은 방식이라고 한다

    return render(request, 'matteapp/results.html', {'choices': choices})
