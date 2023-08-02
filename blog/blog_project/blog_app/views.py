from django.shortcuts import render,redirect
from django.views import View
from blog_app.service import (userLoginService,BlogListServices)
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def login_View(request):
    if request.method == 'POST':
        return userLoginService.userAuthentication(request)
    elif request.method == 'GET':
        return render (request=None,template_name='login.html',)
    
@csrf_exempt
def  signup_View(request):
    if request.method == 'POST':
        return userLoginService.adduser(request=request)
    elif request.method == 'GET':
        return render (request=None,template_name='signup.html')
    
def home_View(request):
    return redirect ('Signup-View')

def blogList_View(request,userid):
    return BlogListServices.getAllBlog(request,userid)

