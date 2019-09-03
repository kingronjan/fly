import os
import uuid
import json

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.templatetags.static import static

from justform.register import RegisterForm
from utils.misc import create_random_captcha

# Create your views here.

def index(request):
    return render(request, 'web/index.html')


def join(request):
    """join"""
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            return render(request, 'web/index.html')
        else:
            return render(request, 'web/join.html', {'form': register_form})

    register_form = RegisterForm()
    return render(request, 'web/join.html', {'form': register_form})


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


def captcha(request):
    """captcha"""
    text, captcha = create_random_captcha()
    request.session['captcha'] = text
    return HttpResponse(captcha.getvalue())