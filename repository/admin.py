from django.contrib import admin
from repository import models

# Register your models here.

admin.register(models.User)
admin.register(models.Blog)