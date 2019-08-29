from django.contrib import admin
from repository import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Blog)
admin.site.register(models.Theme)
admin.site.register(models.Repoting)
admin.site.register(models.Classification)
admin.site.register(models.Tag)
admin.site.register(models.Article)
admin.site.register(models.LikeToArticle)
admin.site.register(models.Comment)