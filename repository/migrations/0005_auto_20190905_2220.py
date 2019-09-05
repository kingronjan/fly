# Generated by Django 2.2.4 on 2019-09-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_auto_20190904_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='down_count',
            field=models.IntegerField(default=0, verbose_name='踩数量'),
        ),
        migrations.AddField(
            model_name='article',
            name='up_count',
            field=models.IntegerField(default=0, verbose_name='点赞数量'),
        ),
        migrations.AddField(
            model_name='user',
            name='registration_time',
            field=models.DateTimeField(auto_now=True, verbose_name='注册时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
    ]
