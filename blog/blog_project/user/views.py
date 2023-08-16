from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from user.service import (userLoginService,userProfileService)

def home_View(request):
    return redirect ('Login-View')

@csrf_exempt
def login_View(request):
    if request.method == 'POST':
        return userLoginService.userAuthentication(request)
    elif request.method == 'GET':
        title='BlogNest : Login '
        return render (request=None,template_name='login.html',context={'title':title})
    
@csrf_exempt
def  signup_View(request):
    if request.method == 'POST':
        return userLoginService.adduser(request=request)
    elif request.method == 'GET':
        title='BlogNest : Sign Up '
        return render (request=None,template_name='signup.html',context={'title':title})
    
def logout_view(request):
    return userLoginService.logoutUser(request)

@csrf_exempt
def user_Profile_View(request,userid):
    if request.method == 'POST':
        return userProfileService.updateUser(request,userid)
    elif request.method == 'GET':
        return userProfileService.getProfile(request,userid)