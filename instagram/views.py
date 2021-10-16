from django.shortcuts import render,redirect
from django.urls import reverse

from django.template import loader, Context
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .models import Post, Profile, Comment, Like
from .forms import PostForm, ProfileForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    template = loader.get_template('insta/home.html')

    if request.user.is_anonymous:
        context = {}
        return HttpResponse(template.render(context, request))

    posts = Post.objects.all()
    profile = Profile.objects.get(user=request.user)
    comments = Comment.objects.all()
    context = {'posts': posts, 'profile': profile, 'comments': comments}
    return HttpResponse(template.render(context, request))

# login
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("user logged in ")
    else:
        return HttpResponse("user ot logged in ")

def signup(request):
    pass

# user profile
def user_profile(request, username):
    template = loader.get_template('insta/profile.html')
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(author__user__username=request.user.username)
    # posts = Post.objects.all()
    context = {'profile': profile, 'posts': posts}
    return HttpResponse(template.render(context, request))