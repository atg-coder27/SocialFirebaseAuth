from datetime import time
from time import sleep
from logging import log
from ntpath import join
from django.contrib import auth
from django.core.exceptions import EmptyResultSet, RequestAborted
from django.shortcuts import render
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.models import User

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.http import HttpResponse,HttpResponseRedirect
from django.template.response import TemplateResponse
from config.firebase_config import firebase_database,firebase_authe
from .forms import *
import json



class Home(View):
    def get(self,request):
        if request.user.is_authenticated:
            return TemplateResponse(request,'dashboard.html')
        return TemplateResponse(request,'home.html')
        
    template_name = "home.html"

class Signup(View):
    def get(self,request):
        fm = UserForm()
        print(request.user)
        return TemplateResponse(request,"signup.html",{"form" : fm})
    
    def post(self,request):
        try:
            fm = UserForm(data = request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                email = fm.cleaned_data['email']
                password = fm.cleaned_data['password']
                user = firebase_authe.create_user_with_email_and_password(email,password)
                user = User.objects.create_user(username = username, password = password, email = email)
                
                return HttpResponse(json.dumps({"message" : "ok"}))
        except Exception as E:
            return HttpResponse(json.dumps({"error" : True, "message" : str(E)}))

class Login(View):
    def get(self,request):
        fm = UserForm()
        return TemplateResponse(request,"login.html",{"form" : fm})
    
    
    def post(self,request):
        try:
            fm = UserForm(data = request.POST)
            if fm.is_valid():
                email = fm.cleaned_data['email']
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = firebase_authe.sign_in_with_email_and_password(email,password)
                if user:
                    user = authenticate(username = username , password = password)
                    if user:
                        login(request,user)
                        return HttpResponse(json.dumps({"message" : "User successfully logged in"}))
                    return HttpResponse(json.dumps({"message" : "User credentials wrong"}))
                else:
                    return HttpResponse(json.dumps({"message": "User not found"}))
                
                # print(request.session.__dict__)
                # logout(request)
                # print(request.session.__dict__)
                # print(request.session.get_expiry_age())
                # cur = 0
                # for i in range(int(1e8)):
                #     cur += i*i
                # print(request.session.get_expiry_age())

                # print(request.user)
                # print(request.user.is_authenticated)
                

        
        except Exception as E:
            return HttpResponse(json.dumps({"error": True, "message" : str(E)}))


class Logout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/')

class DashBoard(View):
    def get(self,request):
        if request.user.is_authenticated:
            return TemplateResponse(request,"dashboard.html")
        return HttpResponseRedirect('/')


class LoginRedirect(View):
    def get(self,request):
        return HttpResponseRedirect('/login/')

class SignRedirect(View):
    def get(self,request):
        return HttpResponseRedirect('/signup/')

class Check(View):
    def get(self,request):
        print(request.session)
        print(request.session.__dict__)
        print(request.user)
        print(request.user.is_authenticated)
        return HttpResponse({"data" : "Ansh"})