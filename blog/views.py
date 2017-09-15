from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
import json
from blog.models import *

User = get_user_model()


def index(request):
    categories = Category.objects.all()
    articles = Post.objects.all()
    return render_to_response('blog/index.html', locals())


@ csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        userquery = User.objects.filter(username=username)
        for user in userquery:
            if user is not None and user.check_password(password):
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                auth.login(request, user)
                return HttpResponseRedirect("../")
        return HttpResponse(json.dumps({'error': 'User not exist'}))
    return render_to_response("blog/login.html")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("../")


def register(request):
    return render_to_response("blog/register.html")
    return HttpResponseRedirect("../")


def edit(request):
    pass


def category(request, slug):
    cur_category = get_object_or_404(names=slug)
    return render_to_response()


def article(request, slug):
    pass