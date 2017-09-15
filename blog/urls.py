from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^edit/$', edit, name='edit'),
    url(r'^category/(?P<slug>[-\w]+)/$', category, name='category'),
    url(r'^article/(?P<slug>[-\w]+)/$', article, name='category'),
]
