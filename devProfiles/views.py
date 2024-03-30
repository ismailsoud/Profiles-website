from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Users
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import math,random
obj=""

def home(request):
    users_data = Users.objects.all()
    return render(request, "home.html", {"users": users_data})
def login(request):
    if request.method == "POST":
        userid = request.POST["userid"]
        password = request.POST["password"]
        try:
            user = Users.objects.get(email=userid)
        except Users.DoesNotExist:
            messages.error(request, 'Wrong Email or Password')
            return render(request, "login.html")
        
        if user.password == password:
            global obj
            obj = user
            return redirect("user")
        else:
            messages.error(request, 'Wrong Email or Password')
            return render(request, "login.html")
    else:
        return render(request, "login.html")

def user(request):
    global obj
    users_data = Users.objects.all()
    return render(request,"userpage.html",{"object":obj,"users": users_data})
def profile(request):
    global obj
    return render(request,"profile.html",{"object":obj})
def logout(request):
    users_data = Users.objects.all()
    return render(request, "home.html", {"users": users_data})

def register(request):
    if request.method=="POST":
       name=request.POST["name"]
       email=request.POST["email"]
       about=request.POST["about"]
       password=request.POST["password"]
       if Users.objects.filter(email=email).exists():
           messages.info(request,"User already exists")
           return render(request,"register.html")
       else:
           d=Users.objects.create(name=name,about=about,email=email,password=password)
           d.save()
           messages.success(request, 'Successfully Register!')
           return render(request, "login.html")
    else:
        return render(request,"register.html")

def edit(request):
    global obj
    if request.method == "POST":
       obj.name=request.POST["name"]
       obj.email=request.POST["email"]
       obj.about=request.POST["about"]
       obj.save()
       return render(request,"profile.html",{"object":obj})
    else:
       return render(request,"edit.html",{"object":obj})
def dellProfile(request):
    if request.method == "POST":
        userid = request.POST.get("userid")
        user = Users.objects.get(email=userid)
        user.delete()
        users_data = Users.objects.all()
        return render(request, "home.html", {"users": users_data})
def photoedit(request):
    if 'image' in request.FILES:
       global obj
       obj.photo.delete(save=True)
       obj.photo=request.FILES["image"]
       obj.save()
    return render(request,"edit.html",{"object":obj})