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
    





    cover_national = getNews(1,2)
    cover_international = getNews(2,2)
    cover_sport = getNews(3,2)
    cover_bussiness = getNews(5,2)
    cover_tech = getNews(5,2)
    cover_life = getNews(5,2)
    

    

    template = loader.get_template('news/cover.html')
    context = {
        'cover_main_news': latest_cover_list[0],
        'cover_main_news_b': latest_cover_list[1],
        'cover_main_news_c': [latest_cover_list[2], latest_cover_list[3]],
        'cover_national_b': cover_national[0],
        'cover_national_c': [cover_national[1], cover_national[2]],
        'cover_international': cover_international[0],
        'cover_sport_b': cover_sport[0],
        'cover_sport_c': [cover_sport[1], cover_sport[2]],
        'cover_bussiness': cover_bussiness[0],
        'cover_tech_b': cover_tech[0],
        'cover_life_b': cover_life[0]
    }
    return HttpResponse(template.render(context, request))

    #output = ','.join([ str(n.category.category) for n in cover_national])
    #return HttpResponse(output)


def category(request, category_id):
    main_news = getNews(category_id, 2)
    list_news = getNews(category_id, 2)
    last_news = News.objects.all()[:5]
    

 
    template = loader.get_template('news/cover-category.html')
    context = {
        'main_news_b': main_news[1],
        'main_news_c': [main_news[2], main_news[3]],
        'news_list': list_news,
        'last_news': last_news
    }
    return HttpResponse(template.render(context, request))

    #output = ','.join([ str(n.category.category) for n in cover_national])
    #return HttpResponse(output)

def single(request, news_id):
    #return HttpResponse("You're looking at news %s." % news_id)


    news = News.objects.get(pk=news_id)
    list_news = getNews(news.category.id, 2)
    last_news = News.objects.all()[:5]
    

 
    template = loader.get_template('news/single.html')
    context = {
        'main_news_b': list_news[1],
        'main_news_c': [list_news[2], list_news[3]],
        'news': news,
        'last_news': last_news
    }
    return HttpResponse(template.render(context, request))




def detail(request, question_id):
    return HttpResponse("You're looking at news %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of news %s."
    return HttpResponse(response % question_id)



def getNews(id_param, status):
    national = News.objects.filter(category__id= id_param).filter(status = status)
    return national
