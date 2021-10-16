from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm
from instagram.models import Profile

# signup request

def signup(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']