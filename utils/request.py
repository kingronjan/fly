from django.shortcuts import redirect, reverse
from functools import wraps


def require_signin(func):
    """为需要登录才能继续操作的页面写的装饰器"""
    @wraps(func)
    def rl(request, *args, **kwargs):
        if not 'user' in request.session:
            return redirect(reverse('web:signin'))
        return func(request, *args, **kwargs)
    return rl