from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponse


def index(request):
    latest_questions = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html', {'latest_questions': latest_questions})


def detail(request, question_id):
    detail = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'detail': detail})


def result(request, question_id):
    return HttpResponse("This is the result for question no. %s" % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting for question %s" % question_id)
