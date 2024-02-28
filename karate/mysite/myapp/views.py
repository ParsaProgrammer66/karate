from django.shortcuts import render,redirect
from .models import Gym,Account
from .forms import SignupForm,CoachForm,LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST,request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            user=User.objects.create_user(cd['username'],cd['email'],cd['password'])
            user.save()
            return redirect('lider')
    else:
        form=SignupForm()
    return render(request,'myapp/signup.html',context={'form':form})


def gym(request):
    coach_field=CoachForm(request.POST,request.FILES)
    if request.method=='POST':
        if coach_field.is_valid():
            coach_field.save()
            return redirect('index')
        
    else:
        coach_field=CoachForm()
    return render(request,'myapp/gym.html',{'coach_field':coach_field})

def member(request):
    coach=Gym.objects.all()
    return render(request,'myapp/member.html',{'coach':coach})

def lider(request):
    return render(request,'myapp/lider.html')


def index(request):
    coach=Gym.objects.all()
    return render(request,'myapp/index.html',{'coach':coach})

def user_login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('invalid')
    else:
        form =LoginForm()
    return render(request,'myapp/login.html',{'form':form})

def hello(request):
    return render(request,'myapp/hello.html')