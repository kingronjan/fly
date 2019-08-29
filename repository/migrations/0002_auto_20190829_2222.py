# Generated by Django 2.2.4 on 2019-08-29 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('summary', models.CharField(max_length=256, null=True, verbose_name='摘要')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='主题名称')),
                ('addr', models.CharField(max_length=128, verbose_name='主题地址')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='头像',
        ),
        migrations.RemoveField(
            model_name='user',
            name='密码',
        ),
        migrations.RemoveField(
            model_name='user',
            name='用户名',
        ),
        migrations.RemoveField(
            model_name='user',
            name='邮箱',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='邮箱'),
        ),
        migrations.AddField(
            model_name='user',
            name='fans',
            field=models.ManyToManyField(related_name='_user_fans_+', to='repository.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='/statics/web/avatars/default-avatar.jpg', upload_to='statics/web/avatars', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='1234', max_length=32, verbose_name='密码'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='fly', max_length=16, verbose_name='用户名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.CharField(max_length=128, null=True, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='theme',
            field=models.CharField(max_length=16, verbose_name='主题'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=32, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='uid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.User', verbose_name='用户ID'),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='标题')),
                ('caption', models.CharField(max_length=128, null=True, verbose_name='描述')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Repoting',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('detail', models.CharField(max_length=512, verbose_name='详情')),
                ('status', models.IntegerField(choices=[(1, '待处理'), (2, '处理中'), (3, '已处理')], verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('process_time', models.DateTimeField(auto_now=True, verbose_name='处理时间')),
                ('processor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pid', to='repository.User', verbose_name='处理人')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uid', to='repository.User', verbose_name='提交人')),
            ],
        ),
        migrations.CreateModel(
            name='LikeToArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_or_dislike', models.BooleanField(verbose_name='赞或踩')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Article', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.User', verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=512, verbose_name='评论详情')),
                ('create_time', models.DateTimeField(verbose_name='评论时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Article', verbose_name='评论文章')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Comment', verbose_name='父级评论ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.User', verbose_name='评论者')),
            ],
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='标题')),
                ('caption', models.CharField(max_length=128, null=True, verbose_name='描述')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Blog', verbose_name='博客ID')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='classification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.Classification', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='t', to='repository.Tag', verbose_name='标签'),
        ),
        migrations.AddConstraint(
            model_name='liketoarticle',
            constraint=models.UniqueConstraint(fields=('article_id', 'user_id'), name='unique_a2u'),
        ),
    ]
