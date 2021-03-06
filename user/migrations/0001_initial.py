# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-13 22:08
from __future__ import unicode_literals

import DjangoUeditor.models
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nick_name', models.CharField(default='好学长', max_length=50, verbose_name='呢称')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别')),
                ('mobile', models.CharField(max_length=11, null=True, verbose_name='手机号')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('context', DjangoUeditor.models.UEditorField(default='', verbose_name='公司介绍')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '关于我们',
                'verbose_name_plural': '关于我们',
            },
        ),
        migrations.CreateModel(
            name='ApplicationCate',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='分类ID')),
                ('name', models.CharField(max_length=50, verbose_name='应用领域名称')),
                ('context', DjangoUeditor.models.UEditorField(default='', verbose_name='具体介绍')),
                ('image', models.ImageField(upload_to='img/%Y/%m', verbose_name='应用领域图片')),
                ('describe', models.CharField(max_length=511, verbose_name='描述')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '应用领域分类',
                'verbose_name_plural': '应用领域分类',
            },
        ),
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='代理品牌')),
                ('describe', models.CharField(max_length=255, verbose_name='描述')),
                ('logo', models.ImageField(upload_to='img/%Y/%m', verbose_name='品牌logo')),
                ('url', models.URLField(verbose_name='代理品牌网页地址')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '客户案例',
                'verbose_name_plural': '客户案例',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='文章标题')),
                ('describe', models.CharField(max_length=255, verbose_name='描述')),
                ('isImportant', models.BooleanField(default=False, verbose_name='是否添加为首页大图新闻')),
                ('picture', models.ImageField(upload_to='img/%Y/%m', verbose_name='首页大图')),
                ('image', models.ImageField(upload_to='img/%Y/%m', verbose_name='新闻图例')),
                ('context', DjangoUeditor.models.UEditorField(default='', verbose_name='文章内容')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('click_count', models.IntegerField(default=0, verbose_name='点击数')),
            ],
            options={
                'verbose_name': '新闻动态',
                'verbose_name_plural': '新闻动态',
            },
        ),
        migrations.CreateModel(
            name='ProductMainCate',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='分类ID')),
                ('name', models.CharField(max_length=50, verbose_name='产品分类')),
                ('image', models.ImageField(upload_to='img/%Y/%m', verbose_name='类别图片')),
                ('describe', models.CharField(max_length=511, verbose_name='类别介绍')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '产品分类',
                'verbose_name_plural': '产品分类',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('describe', models.CharField(max_length=511, verbose_name='描述')),
                ('image', models.ImageField(upload_to='img/%Y/%m', verbose_name='案例图片')),
                ('context', DjangoUeditor.models.UEditorField(default='', verbose_name='具体介绍')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '产品详情',
                'verbose_name_plural': '产品详情',
            },
        ),
        migrations.CreateModel(
            name='ProductSecondCate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='细化分类名称')),
                ('describe', models.CharField(max_length=511, verbose_name='类别介绍')),
                ('logo', models.ImageField(upload_to='img/%Y/%m', verbose_name='分类产品logo')),
                ('image', models.ImageField(upload_to='img/%Y/%m', verbose_name='产品图片案例')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('productMainCate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ProductMainCate', verbose_name='产品分类')),
            ],
            options={
                'verbose_name': '产品具体分类',
                'verbose_name_plural': '产品具体分类',
            },
        ),
        migrations.AddField(
            model_name='products',
            name='productSecondCate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ProductSecondCate', verbose_name='细化分类'),
        ),
    ]
