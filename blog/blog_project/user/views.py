from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from user.service import (userLoginService)
from blog_app.service import getUser
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

def user_Profile_View(request,userid):
    if request.method == 'POST':
        return
    elif request.method == 'GET':
        data=getUser(userid)
        title= (f"{data['userfullname']}| BlogNest")
        return render (request=None,template_name='user_profile.html',context={'title':title,'userid':userid})