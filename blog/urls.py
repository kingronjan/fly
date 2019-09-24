from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', views.apply, name='apply'),
    path('test/', views.test, name='test'),
    path('<str:username>/article/', views.article, name='article'),
]
