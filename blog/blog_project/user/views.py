from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from user.service import (userLoginService,userProfileService,validateToken,loginCoreService)
from django.views import View

def home_View(request):
    return redirect ('Login-View')

# class LoginView(View):
#     def get(cls,request):
#         return userLoginService.userAuthentication(request)
    
#     
#     def post(cls,request):
#         title='BlogNest : Login'
#         msg = request.session.get('message')
#         return render (request,template_name='login.html',context={'title':title,'message':msg})

def login_View(request):
    if request.method == 'POST':
        return userLoginService.userAuthentication(request)
    elif request.method == 'GET':
        title='BlogNest : Login'
        msg = request.session.get('message')
        return render (request,template_name='login.html',context={'title':title,'message':msg})
    
def forgetpassword_View(request):
    if request.method == 'POST':
        # return userLoginService.userAuthentication(request)
        pass
    elif request.method == 'GET':
        title='BlogNest : Forget Password'
        msg = request.session.get('message')
        return render (request,template_name='forgot_password.html',context={'title':title,'message':msg})
    

def  signup_View(request):
    if request.method == 'POST':
        return userLoginService.adduser(request=request)
    elif request.method == 'GET':
        title='BlogNest : Sign Up '
        return render (request,template_name='signup.html',context={'title':title})



def logout_view(request):
    return userLoginService.logoutUser(request)


def availablityUsername(request):
    return loginCoreService.userNameAvailability(request)


def availablitymail(request):
    return loginCoreService.mailAvailability(request)



@validateToken
def user_Profile_View(request,userid):
    if request.method == 'POST':
        return userProfileService.updateUser(request,userid)
    elif request.method == 'GET':
        return userProfileService.getProfile(request,userid)