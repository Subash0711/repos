from django.shortcuts import render,redirect
from Users.models import Users
from Users.service import userRegisterService,userLoginService
# Create your views here.
def userRegistration_view(request):
     if request.method=='POST':  
        return userRegisterService.adduser(request)
     if request.method=='GET':
        return render (request,'registration_template.html')
def userLogin_view(request):
    if request.method=='POST': 
        return userLoginService.userAuthentication(request)
    if request.method=='GET':
        return render (request,'login_template.html')  

