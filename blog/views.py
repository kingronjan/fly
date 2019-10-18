from django.shortcuts import render
from repository import models
from utils.request import require_signin
from utils.error import render404

# Create your views here.

def index(request, username):
    user = models.User.objects.filter(username=username).first()
    blog = models.Blog.objects.filter(user=user).first()
    if not blog:
        # return redirect(reverse('blog:apply'))
        return render404(request)

    articles = models.Article.objects.filter(blog=blog)
    return render(request, 'blog/homepage.html', {'user': user, 'blog': blog, 'articles': articles})


@require_signin
def apply(request):
    from justform.blog import BlogForm
    user = request.session['user']
    blog = models.Blog.objects.filter(user__username=user).first()
    if blog:
        return index(request, user)

    if request.method != 'POST':
        form = BlogForm()
        return render(request, 'blog/apply.html', {'form': form})

    form = BlogForm(request.POST)
    if not form.is_valid():
        return render(request, 'blog/apply.html', {'form': form})

    suffix = request.session['user']
    user = models.User.objects.filter(username=suffix).first()
    data = form.cleaned_data
    models.Blog.objects.create(suffix=suffix, user=user, title=data['title'], summary=data['summary'])

    return index(request, user)


def test(request):
    return render(request, 'blog/layout.html')


def user_article(request, username):
    user = models.User.objects.filter(username=username).first()
    articles = models.Article.objects.filter(author=user)
    print(articles)
    return render(request, 'blog/articlemanage.html', {'articles': articles, 'user': user})


def article_detail(request, aid):
    article = models.Article.objects.filter(id=aid).first()
    if not article:
        return render404(request)
    return render(request, 'blog/article.html', {'article': article})