from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('apply/', views.apply, name='apply'),
    path('test/', views.test, name='test'),
    path('home/<str:username>/', views.index, name='index'),
    path('home/<str:username>/article/', views.user_article, name='article'),
    path('article/<int:aid>', views.article_detail, name='article'),
]
