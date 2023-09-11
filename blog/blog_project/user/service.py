from typing import Any
import jwt
import datetime
from user.models import (BlogUsers)
from blog_app.models import (BlogLists,BlogUserComments)
from django.contrib.auth.hashers import make_password,check_password
from django.urls import reverse
from django.shortcuts import render,redirect
from blog_app.service import coreservices
from django.db import IntegrityError
from . import messages
from django.http import JsonResponse,HttpResponse
from blog_app.service import blogCoreService

class loginCoreService:
    def userNameAvailability(request):
        userVal= request.POST.get('username')
        usernameCount=BlogUsers.objects.filter(username=userVal).count()
        if usernameCount == 0:
            return JsonResponse({'available':True})
        else:
            return JsonResponse({'available':False})
    
    def mailAvailability(request):
        userVal= request.POST.get('email')
        mailCount=BlogUsers.objects.filter(emailid=userVal).count()
        if mailCount == 0:
            return JsonResponse({'available':True})
        else:
            return JsonResponse({'available':False})
    
class userLoginService:
    @classmethod
    def userAuthentication(cls,request):
        username=request.POST.get('username')
        password=request.POST.get('userpassword')
        
        existUser=BlogUsers.objects.filter(username=username).first()
        if existUser:
            hashPassword=existUser.password
            if check_password(password,hashPassword):
                    userid=existUser.id
                    payload={'user_id':userid}
                    access_token=TokenService.genrateToken(data=payload,expiryin=1)
                    request.session['access_token'] = access_token
                    url=reverse('BlogList_View',kwargs={'userid':userid})
                    return redirect(url)
            return render(request,'login.html',{'exception':messages.INCORRECT_PASSWORD_MSG})
        else:
            return render(request,'login.html',{'exception':messages.INCORRECT_USERNAME_MSG})
            
    @classmethod
    def adduser(cls,request):
        try:
            fullname=request.POST.get('full_name')
            emailId=request.POST.get('email_address')
            gender=request.POST.get('usergender')
            username=request.POST.get('user_name')
            phonenumber=request.POST.get('phone_number')
            password=request.POST.get('user_password')
            encPassword=make_password(password=password)
            data=BlogUsers(fullname=fullname,gender=gender,emailid=emailId,username=username,mobile_no=phonenumber,password=encPassword)
            data.save()
            url= reverse('Login-View')
            request.session['message'] = messages.CREATE_USER_SUCCESS_MSG
            return redirect(url)
        except IntegrityError:
            return HttpResponse()
        
    @classmethod
    def logoutUser(cls,request):
        request.session.clear()
        return redirect('Login-View')
    
class userProfileService: 
    @classmethod
    def getProfile(cls,request,userid):
        data=coreservices.getUser(userid)
        blogCount=blogCoreService.getBlogsCount(userid)
        blogcmtCount=blogCoreService.getCommentsCount(userid)
        UserGetLikesCount=blogCoreService.getLikesCount(userid)
        title= (f"{data['userfullname']}| BlogNest")
        msg  = request.session.get('message')
        return render (request=None,template_name='user_profile.html',context={'title':title,'userid':userid,'message':msg,'user':data,'userblogCount':blogCount,'userCmtsCount':blogcmtCount,'userGetLikesCount':UserGetLikesCount['likes']})
     
    @classmethod
    def updateUser(cls,request,userid):
        columnName=request.POST.get('column-name')
        userdata=BlogUsers.objects.get(id=userid)
        data=coreservices.getUser(userid)
        blogCount=blogCoreService.getBlogsCount(userid)
        blogcmtCount=blogCoreService.getCommentsCount(userid)
        UserGetLikesCount=blogCoreService.getLikesCount(userid)
        if columnName == 'password-col':
            oldPassword=request.POST.get('old-password')
            newPassword=request.POST.get('new-password')
            hashedPassword=userdata.password
            if check_password(oldPassword,hashedPassword):
                encpasword=make_password(newPassword)
                userdata.password=encpasword
                userdata.save()
                url=reverse('User-Profile-View',kwargs={'userid':userid})
                request.session['message'] = messages.PASSWORD_UPDATE_MSG
                return redirect(url)
            msg={'errormessage':messages.PASSWORD_CHECK_MSG,'userid':userid,'user':data,'userblogCount':blogCount,'userCmtsCount':blogcmtCount,'userGetLikesCount':UserGetLikesCount['likes']}
            return render(request=None,template_name='user_profile.html',context=msg)
        elif columnName == 'contact-col':
            updateName=request.POST.get('update-full-name')
            updateMobileNo=request.POST.get('update-mobile-no')
            updateEmail=request.POST.get('update-email')    

            userdata.fullname=updateName
            userdata.mobile_no=updateMobileNo
            userdata.emailid=updateEmail
            userdata.save()
            url=reverse('User-Profile-View',kwargs={'userid':userid})
            request.session['message'] = messages.DETAILS_UPDATE_MSG
            return redirect(url)   
        elif columnName == 'username-col':
            updateUsername=request.POST.get('update-user-name')
            userNameCount=BlogUsers.objects.filter(username=updateUsername).count()
            if userNameCount == 0:
                userdata.username=updateUsername
                userdata.save()
                url=reverse('User-Profile-View',kwargs={'userid':userid})
                request.session['message'] = messages.USERNAME_UPDATE_MSG
                return redirect(url)
            msg={'errormessage':messages.USERNAME_UNAVAILABLE_MSG,'userid':userid,'user':data,'userblogCount':blogCount,'userCmtsCount':blogcmtCount,'userGetLikesCount':UserGetLikesCount}
            return render(request=None,template_name='user_profile.html',context=msg)
        
class TokenService:

    SECRET_KEY='djanagoblogNestSecretKeyIsopojjsjvdvdsvdvdvdsv'

    @staticmethod
    def genrateToken(data,expiryin):
        expiryTime=datetime.datetime.utcnow()+datetime.timedelta(hours=expiryin)
        payload={
            'exp':expiryTime,
            **data
        }
        return jwt.encode(payload,TokenService.SECRET_KEY,algorithm='HS256')
    
def validateToken(view_func):
    def wrappedView(request,*args,**kwargs):
        token = request.session.get('access_token')
        try:
            jwt.decode(token,TokenService.SECRET_KEY,algorithms='HS256')
            return view_func(request,*args,**kwargs)
        except jwt.ExpiredSignatureError:
            cntxdata={'title':'405 Method Not Allowed','content':'Request Time has been Expired','StatusCode':'405'}
            return render(request=None,template_name='user_error.html',context=cntxdata)
        except jwt.InvalidTokenError:
            cntxdata={'title':'401 Unauthorized','content':'Unauthorized Request has been Found','StatusCode':'401'}
            return render(request=None,template_name='user_error.html',context=cntxdata)
    return wrappedView
        