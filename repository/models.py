from django.db import models

# Create your models here.


class User(models.Model):
    """Users"""
    username = models.CharField(max_length=16, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=32, verbose_name='密码')
    email = models.EmailField(null=True, verbose_name='邮箱')
    image = models.ImageField(default='web/avatars/default-avatar.jpg',
                              upload_to='web/avatars',
                              verbose_name='头像')
    fans = models.ManyToManyField('self', related_name='fan')

    def __str__(self):
        return self.username


class Blog(models.Model):
    suffix = models.CharField(max_length=16)
    theme = models.CharField(max_length=16, verbose_name='主题')
    title = models.CharField(max_length=32, verbose_name='标题')
    summary = models.CharField(max_length=128, null=True, verbose_name='简介')
    uid = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户ID')

    def __str__(self):
        return self.title


class Theme(models.Model):
    name = models.CharField(max_length=16, verbose_name='主题名称')
    addr = models.CharField(max_length=128, verbose_name='主题地址')

    def __str__(self):
        return self.name


class Repoting(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=32, verbose_name='标题')
    detail = models.CharField(max_length=512, verbose_name='详情')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uid', verbose_name='提交人')
    processor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='pid', verbose_name='处理人')

    status_choice = (
        (1, '待处理'),
        (2, '处理中'),
        (3, '已处理')
    )
    status = models.IntegerField(choices=status_choice, verbose_name='状态')

    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    process_time = models.DateTimeField(auto_now=True, verbose_name='处理时间')

    def __str__(self):
        return self.title


class Classification(models.Model):
    title = models.CharField(max_length=16, verbose_name='标题')
    caption = models.CharField(max_length=128, null=True, verbose_name='描述')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='博客ID')

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=16, verbose_name='标题')
    caption = models.CharField(max_length=128, null=True, verbose_name='描述')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    summary = models.CharField(max_length=256, null=True, verbose_name='摘要')
    content = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(verbose_name='创建时间')
    classification = models.ForeignKey(Classification, null=True, on_delete=models.SET_NULL, verbose_name='分类')
    tag = models.ManyToManyField(Tag, related_name='t', verbose_name='标签')

    def __str__(self):
        return self.title


class LikeToArticle(models.Model):

    class Meta:
        constraints = [models.UniqueConstraint(fields=['article_id', 'user_id'], name='unique_a2u')]

    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    like_or_dislike = models.BooleanField(verbose_name='赞或踩')


class Comment(models.Model):
    content = models.CharField(max_length=512, verbose_name='评论详情')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='评论文章')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论者')
    create_time = models.DateTimeField(verbose_name='评论时间')
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, verbose_name='父级评论ID')

    def __str__(self):
        return self.content