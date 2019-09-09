from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signin/checkusername/', views.checkusername, name='checkusername'),
    path('signout/', views.signout, name='signout'),
    path('apply-blog/', views.apply_blog, name='apply-blog'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('captcha/', views.handle_captcha, name='captcha'),
    path('<str:username>', views.homepage, name='homepage'),
]