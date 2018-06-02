from django.urls import path 

from . import views 

urlpatterns = [
	path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('news/<int:news_id>/', views.single, name='single'),
    path('contacto/', views.contacto, name='contacto')
]