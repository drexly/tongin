#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.http import HttpResponse
from dosirak.models import Question
from django.template import RequestContext, loader

def index(request):
    question_list=Question.objects.order_by('-pub_date')[:]
    #template = loader.get_template('dosirak/index.html')
    #context = RequestContext(request, {
    #    'question_list': question_list,
    #})
    context={'question_list':question_list}
    #return HttpResponse(output+template.render(context))
    return render(request, 'dosirak/index.html', context)

def detail(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request, 'dosirak/detail.html', {'question':question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)