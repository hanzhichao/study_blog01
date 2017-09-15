# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ('-comment_time',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('names', models.CharField(max_length=20, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b\xe5\x90\x8d\xe7\xa7\xb0')),
                ('desc', models.TextField(null=True, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('body', models.TextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xb8\x80\xe6\xac\xa1\xe4\xbf\xae\xe6\x94\xb9')),
                ('status', models.CharField(max_length=1, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'P', b'\xe5\xb7\xb2\xe5\x8f\x91\xe5\xb8\x83'), (b'D', b'\xe5\xb7\xb2\xe5\x88\xa0\xe9\x99\xa4'), (b'E', b'\xe7\xbc\x96\xe8\xbe\x91\xe4\xb8\xad')])),
                ('views', models.PositiveIntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name=b'\xe5\x96\x9c\xe6\xac\xa2')),
                ('praises', models.PositiveIntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe8\xb5\x9e')),
                ('category', models.ManyToManyField(to='blog.Category', blank=True)),
                ('user', models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-create_time',),
            },
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0', to='blog.Post'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
    ]
