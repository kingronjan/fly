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


class Blog(models.Model):
    suffix = models.CharField(max_length=16)
    theme = models.CharField()
    title = models.CharField(max_length=32)
    summary = models.CharField(max_length=128)
    uid = models.ForeignKey(User, on_delete=True, unique=True)
