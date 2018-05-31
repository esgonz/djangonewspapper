from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 
def index(request):
	return HttpResponse("Hellow, world. You are in a website news") 

def detail(request, question_id):
    return HttpResponse("You're looking at news %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of news %s."
    return HttpResponse(response % question_id)

def eduardo(request, age):
	response ="Hola Eduardo tu edad es %d"
	return HttpResponse(response %age)
