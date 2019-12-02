from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User_Data
# Create your views here.


def login(request):
    return render(request, 'login.html')


def mail(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    username = request.POST.get('username')
    if email:
        username = email.split('@')[0]

    mode = request.POST.get('mode')
    if mode == "signup":
        User.objects.create_user(
            username=username, email=email, password=password)
    if mode == "signin":
        username = username.split('@')[0]
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return HttpResponseRedirect('/')
    context = {
        'username': username,
        'mode': mode,
    }
    return render(request, 'mail.html', context)


data = {}


def home(request):
    username = request.POST.get('username')
    if username:
        data.setdefault('username', username)
        data.setdefault('first_name', request.POST.get('first_name'))
        data.setdefault('last_name', request.POST.get('last_name'))
        data.setdefault('college', request.POST.get('college'))
        data.setdefault('qualification', request.POST.get('qualification'))
        data.setdefault('contact', request.POST.get('contact'))

    pref = request.POST.get('pref')
    if pref:
        data.setdefault('pref', pref)
    if data.get('pref'):
        User_Data.objects.create(username=data['username'], first_name=data['first_name'],
                                 last_name=data['last_name'], college=data['college'], qualification=data['qualification'], contact=data['contact'], preferences=data['pref'])
        data.clear()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'home.html')


def profile(request):
    user_d = User_Data.objects.get(user=request.user)
    user = User.objects.get(username=request.user)
    if request.POST:
        user_d.username = request.POST.get('username')
        user_d.first_name = request.POST.get('first name')
        user_d.last_name = request.POST.get('last name')
        user_d.college = request.POST.get('institution')
        user_d.qualification = request.POST.get('qualification')
        user_d.contact = request.POST.get('contact')
        user.email = request.POST.get('email')
        user_d.save(update_fields=[
                    'username', 'first_name', 'last_name', 'college', 'qualification', 'contact'])
        user.save(update_fields=['email'])
        return HttpResponseRedirect('/')
    context = {
        'email': user.email,
        'user': user_d,
    }
    return render(request, 'profile.html', context)
