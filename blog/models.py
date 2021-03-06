# coding:utf8
from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    names = models.CharField('类型名称', max_length=20)
    desc = models.TextField('分类描述', blank=True, null=True)

    def __unicode__(self):
        return self.names
    

class User(AbstractUser):
    pass


class Post(models.Model):
    POST_STATUS =(
        ('P', '已发布'),
        ('D', '已删除'),
        ('E', '编辑中')
    )

    title = models.CharField('标题', max_length=150)
    body = models.TextField('正文')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modify_time = models.DateTimeField('最后一次修改', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=POST_STATUS)
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('喜欢', default=0)
    praises = models.PositiveIntegerField('点赞', default=0)
    category = models.ManyToManyField('Category', blank=True)
    user = models.ForeignKey('User', verbose_name='作者')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-create_time',)


class BlogComment(models.Model):
    user = models.ForeignKey('User', verbose_name='用户')
    post = models.ForeignKey('Post',verbose_name='文章')
    comment = models.TextField('评论内容', blank=True)
    comment_time = models.DateTimeField('评论时间', auto_now_add=True)

    class Meta:
        ordering = ('-comment_time',)

