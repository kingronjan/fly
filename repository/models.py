from django.db import models

# Create your models here.


class User(models.Model):
    """Users"""
    username = models.CharField(max_length=16, name='用户名')
    password = models.CharField(max_length=32, name='密码')
    email = models.EmailField(null=True, name='邮箱')
    image = models.ImageField(default='/statics/web/avatars/default-avatar.jpg',
                              upload_to='statics/web/avatars',
                              name='头像')
    fans = models.ManyToManyField('self', related_name='fan')


class Blog(models.Model):
    suffix = models.CharField(max_length=16)
    theme = models.CharField(max_length=16, name='主题')
    title = models.CharField(max_length=32, name='标题')
    summary = models.CharField(max_length=128, name='简介')
    uid = models.OneToOneField(User, on_delete=True, name='用户ID')


class Repoting(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=32, name='标题')
    detail = models.CharField(max_length=512, name='详情')
    user = models.ForeignKey(User, on_delete=False)
    processor = models.ForeignKey(User, null=True, on_delete=False)

    status_choice = (
        (1, '待处理'),
        (2, '处理中'),
        (3, '已处理')
    )
    status = models.IntegerField(choices=status_choice, name='状态')

    create_time = models.DateTimeField(auto_now=True, name='创建时间')
    process_time = models.DateTimeField(auto_now=True, name='处理时间')


class Classification(models.Model):
    title = models.CharField(max_length=16, name='标题')
    caption = models.CharField(max_length=128, null=True, name='描述')
    blog = models.ForeignKey(Blog, on_delete=True)


class Tag(models.Model):
    title = models.CharField(max_length=16, name='标题')
    caption = models.CharField(max_length=128, null=True, name='描述')
    blog = models.ForeignKey(Blog, on_delete=True)


class Article(models.Model):
    title = models.CharField(max_length=32, name='标题')
    summary = models.CharField(max_length=256, null=True, name='摘要')
    content = models.TextField(name='内容')
    create_time = models.DateTimeField(name='创建时间')
    classification = models.ForeignKey(Classification, on_delete=True, name='分类')
    tag = models.ManyToManyField(Tag, related_name='t', null=True, name='标签')


class LikeToArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=True, name='文章')
    user = models.ForeignKey(User, on_delete=True, name='用户')
    like_or_dislike = models.BooleanField(name='赞或踩')

    class Meta:
        unique_together = [
            ('article', 'user')
        ]


class Comment(models.Model):
    content = models.CharField(max_length=512, name='评论详情')
    article = models.ForeignKey(Article, on_delete=True, name='评论文章')
    user = models.ForeignKey(User, on_delete=True, name='评论者')
    create_time = models.DateTimeField(name='评论时间')
    parent_id = models.ForeignKey('Comment', on_delete=True, name='父级评论ID')