import os
import uuid
import json

from django.http import Http404
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.templatetags.static import static

from justform.register import RegisterForm
from justform.blog import BlogForm
from utils.misc import create_random_captcha, is_right_captcha
from utils.error import render404

from repository import models


# Create your views here.


def index(request):
    """blog site's index page"""
    return render(request, 'web/index.html')


def homepage(request, username):
    user = models.User.objects.filter(username=username).first()
    if user is None:
        return render404(request)

    return render(request, 'web/homepage.html', {'user_info': user})


def signup(request):
    """join"""
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)

        if not is_right_captcha(request):
            register_form.add_error('captcha', '验证码输入错误')
            return render(request, 'web/signup.html', {'form': register_form})

        if register_form.is_valid():
            register_form.cleaned_data.pop('captcha')
            models.User.objects.create(**register_form.cleaned_data)
            request.session['user'] = register_form.cleaned_data['username']
            return render(request, 'web/index.html')
        else:
            return render(request, 'web/signup.html', {'form': register_form})

    register_form = RegisterForm()
    return render(request, 'web/signup.html', {'form': register_form})


def signin(request):

    def render_err(field, value):
        errors = {field: value}
        # FIXME
        #  NoReverseMatch: Reverse for 'signin' not found.
        # form blog.apply
        return render(request, 'web/signin.html', {'errors': errors})

    if request.method == 'POST':
        if not is_right_captcha(request):
            return render_err('captcha', '验证码输入错误。')

        username = request.POST.get('username')
        saved_user = models.User.objects.filter(username=username)
        if not saved_user:
            return render_err('username', '用户名不存在。')

        password = request.POST.get('password')
        saved_pwd = saved_user.values_list('password')[0][0]
        if saved_pwd != password:
            return render_err('password', '密码错误。')

        if request.POST.get('nosignin1month'):
            request.session.set_expiry(30 * 24 * 60 * 60)

        request.session['user'] = username
        return redirect(reverse('web:homepage'), username=username)

    return render_err(None, None)


def checkusername(request):
    message = {}
    username = request.POST.get('username')
    if not models.User.objects.filter(username=username):
        message['signin_error'] = '用户名不存在。'
    else:
        message['signup_error'] = '用户名已存在。'
    return HttpResponse(json.dumps(message))


def signout(request):
    if 'user' in request.session:
        request.session.pop('user')
    return redirect('/web/')


def upload_image(request):
    nid = str(uuid.uuid4())
    result = {
        'status': True,
        'data': None,
        'message': None
    }
    obj = request.FILES.get('img')
    filepath = os.path.join('web/static/web/avatars/', nid + obj.name)
    with open(filepath, 'wb') as f:
        for line in obj.chunks():
            f.write(line)
    # 去掉前面的 'web' 否则会导致静态文件地址出错
    result['data'] = filepath[3:]
    return HttpResponse(json.dumps(result))


def handle_captcha(request):
    """captcha"""
    text, captcha = create_random_captcha()
    request.session['captcha'] = text
    return HttpResponse(captcha.getvalue())
