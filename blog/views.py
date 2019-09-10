from django.urls import reverse
from django.shortcuts import render, redirect
from repository import models

# Create your views here.


def index(request, blog_info=None):

    return render(request, 'blog/homepage.html', {'blog_info': blog_info})


def apply(request):
    from justform.blog import BlogForm

    if not request.session.get('user'):
        return redirect(reverse('web:signin'))

    if request.method != 'POST':
        form = BlogForm()
        return render(request, 'blog/apply.html', {'form': form})

    form = BlogForm(request.POST)
    if not form.is_valid():
        return render(request, 'blog/apply.html', {'form': form})

    suffix = request.session['user']
    user = models.User.objects.filter(username=suffix).first()
    data = form.cleaned_data
    blog = models.Blog.objects.create(suffix=suffix, user=user, title=data['title'], summary=data['summary'])

    return index(request, blog)