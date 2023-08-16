from user.models import (BlogUsers)
from django.contrib.auth.hashers import make_password,check_password
from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth import logout
from blog_app.service import getUser
from urllib.parse import urlencode,parse_qs,unquote

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
                    url=reverse('BlogList_View',kwargs={'userid':userid})
                    return redirect(url)
            return render(request,'login.html',{'exception':'Please Check your Password'})
        else:
            return render(request,'login.html',{'exception':'Please Check your Username'})
            
    @classmethod
    def adduser(cls,request):
        fullname=request.POST.get('full_name')
        emailId=request.POST.get('email_address')
        gender=request.POST.get('usergender')
        username=request.POST.get('user_name')
        phonenumber=request.POST.get('phone_number')
        password=request.POST.get('user_password')
        encPassword=make_password(password=password)
        data=BlogUsers(fullname=fullname,gender=gender,emailid=emailId,username=username,mobile_no=phonenumber,password=encPassword)
        data.save()
        return redirect('Login-View')
        
    @classmethod
    def logoutUser(cls,request):
        logout(request)
        return redirect('Login-View')
    
class userProfileService: 
    @classmethod
    def getProfile(cls,request,userid):
        data=getUser(userid)
        title= (f"{data['userfullname']}| BlogNest")
        queryParams=parse_qs(request.META['QUERY_STRING'])
        msg=unquote(queryParams.get('message',[''])[0])
        return render (request=None,template_name='user_profile.html',context={'title':title,'userid':userid,'message':msg,'user':data})
     
    @classmethod
    def updateUser(cls,request,userid):
        columnName=request.POST.get('column-name')
        userdata=BlogUsers.objects.get(id=userid)
        if columnName == 'password-col':
            oldPassword=request.POST.get('old-password')
            newPassword=request.POST.get('new-password')
            hashedPassword=userdata.password
            if check_password(oldPassword,hashedPassword):
                encpasword=make_password(newPassword)
                userdata.password=encpasword
                userdata.save()

                url=reverse('User-Profile-View',kwargs={'userid':userid})
                msg={'message':'Password Updated Sucessfully'}
                msg=urlencode(msg)
                url+=f'?{msg}'
                return redirect(url)
            msg={'errormessage':'Please check your old Password','userid':userid}
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
            msg={'message':'Details Updated Sucessfully'}
            msg=urlencode(msg)
            url+=f'?{msg}'
            return redirect(url)
            
        elif columnName == 'username-col':
            updateUsername=request.POST.get('update-user-name')
            userNameCount=BlogUsers.objects.filter(username=updateUsername).count()
            if userNameCount == 0:
                userdata.username=updateUsername
                userdata.save()
                url=reverse('User-Profile-View',kwargs={'userid':userid})
                msg={'message':'Username Updated Sucessfully'}
                msg=urlencode(msg)
                url+=f'?{msg}'
                return redirect(url)
            msg={'errormessage':'Username is not avialbale','userid':userid}
            return render(request=None,template_name='user_profile.html',context=msg)