from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import News
# Create your views here.
#
# 
def index(request):
    latest_question_list = News.objects.order_by('date')[:5]
    template = loader.get_template('news/single.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
	#return HttpResponse(output)
	#return HttpResponse("Hellow, world. You are in a website news") 

def detail(request, question_id):
    return HttpResponse("You're looking at news %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of news %s."
    return HttpResponse(response % question_id)

def eduardo(request, age):
	response ="Hola Eduardo tu edad es %d"
	return HttpResponse(response %age)
