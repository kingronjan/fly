# Generated by Django 2.2.1 on 2019-09-24 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0010_auto_20190924_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='caption',
        ),
    ]
