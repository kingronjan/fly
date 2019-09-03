from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('join/', views.join, name='join'),
    path('upload_image/', views.upload_image, name='upload_image'),
]