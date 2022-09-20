# Generated by Django 3.2.13 on 2022-05-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=128)),
                ('authors', models.CharField(max_length=50)),
                ('publish_date', models.CharField(max_length=50)),
                ('onlineorlocal', models.CharField(choices=[('local', '本地'), ('online', '网络')], default='网络', max_length=32)),
                ('url', models.CharField(max_length=128)),
                ('stardate', models.CharField(max_length=50)),
                ('belonger', models.CharField(max_length=50)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '收藏文章',
                'verbose_name_plural': '收藏文章',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='Article0',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=128)),
                ('authors', models.CharField(max_length=50)),
                ('publish_date', models.CharField(max_length=50)),
                ('onlineorlocal', models.CharField(choices=[('local', '本地'), ('online', '网络')], default='网络', max_length=32)),
                ('url', models.CharField(max_length=128)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='latestdownload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=128)),
                ('authors', models.CharField(max_length=50)),
                ('publish_date', models.CharField(max_length=50)),
                ('onlineorlocal', models.CharField(choices=[('local', '本地'), ('online', '网络')], default='网络', max_length=32)),
                ('belonger', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=128)),
                ('downloaddate', models.CharField(max_length=50)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '最近下载',
                'verbose_name_plural': '最近下载',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='latestread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=128)),
                ('authors', models.CharField(max_length=50)),
                ('publish_date', models.CharField(max_length=50)),
                ('onlineorlocal', models.CharField(choices=[('local', '本地'), ('online', '网络')], default='网络', max_length=32)),
                ('url', models.CharField(max_length=128)),
                ('readdate', models.CharField(max_length=50)),
                ('belonger', models.CharField(max_length=50)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '最近阅读',
                'verbose_name_plural': '最近阅读',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('date', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=256)),
                ('belonger', models.CharField(max_length=50)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '笔记本',
                'verbose_name_plural': '笔记本',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['-c_time'],
            },
        ),
    ]
