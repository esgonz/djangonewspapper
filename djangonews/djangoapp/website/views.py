from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import News
from .models import Cover
from .models import CoverNews
from .models import Category
# Create your views here.
#
# 
def index(request):
    """latest_question_list = News.objects.order_by('date')[:5]
    template = loader.get_template('news/single.html')
    context = {
        'latest_question_list': latest_question_list,
    }"""
    #return HttpResponse(template.render(context, request))
	#return HttpResponse(output)
	#return HttpResponse("Hellow, world. You are in a website news") 
  

    """
    q_latest_cover = Cover.objects.order_by('-date')[:1]
    last_cover_id = q_latest_cover[0].id
    latest_question_list = News.objects.order_by('-date')[:5]
    output = q_latest_cover[0].id
    return HttpResponse(output)"""


    """
    q_latest_cover = Cover.objects.order_by('-date')[:1]
    last_cover_id = q_latest_cover[0].id
    latest_question_list = CoverNews.objects.filter(cover = last_cover_id)[:4]
    output = ','.join([ str(q.news.title) for q in latest_question_list])
    #output = q_latest_cover[0].id
    return HttpResponse(output)
    """

    q_latest_cover = Cover.objects.order_by('-date')[:1]
    last_cover_id = q_latest_cover[0].id
    latest_cover_list = CoverNews.objects.filter(cover = last_cover_id)[:4]
    





    cover_national = News.objects.filter(category__category="Nacional")
    cover_international = News.objects.filter(category__id = 2)[:1]
    cover_sport = News.objects.filter(category__id = 3)[:3]
    cover_bussiness = News.objects.filter(category__id = 5)[:1]
    cover_tech = News.objects.filter(category__id = 5)[:1]
    cover_life = News.objects.filter(category__id = 5)[:1]



    template = loader.get_template('news/contact.html')
    context = {
        'cover_main_news': latest_cover_list[0],
        'cover_main_news_b': latest_cover_list[1],
        'cover_main_news_c': [latest_cover_list[2], latest_cover_list[3]],
        'cover_national_b': latest_cover_list[0],
        'cover_national_c': [latest_cover_list[1], latest_cover_list[2]],
        'cover_innational': cover_international[0],
        'cover_sport_b': cover_sport[0],
        'cover_national_c': [cover_sport[1], cover_sport[2]],
        'cover_bussiness': cover_bussiness[0],
        'cover_tech_c': cover_tech[0],
        'cover_life_c': cover_life[0]
    }
    return HttpResponse(template.render(context, request))






def detail(request, question_id):
    return HttpResponse("You're looking at news %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of news %s."
    return HttpResponse(response % question_id)

def eduardo(request, age):
	response ="Hola Eduardo tu edad es %d"
	return HttpResponse(response %age)
