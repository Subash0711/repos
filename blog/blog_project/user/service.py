from user.models import (BlogUsers)
from django.contrib.auth.hashers import make_password,check_password
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import logout

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
        username=request.POST.get('user_name')
        phonenumber=request.POST.get('phone_number')
        password=request.POST.get('user_password')
        encPassword=make_password(password=password)
        data=BlogUsers(fullname=fullname,emailid=emailId,username=username,mobile_no=phonenumber,password=encPassword)
        data.save()
        return redirect('Login-View')
        
    @classmethod
    def logoutUser(cls,request):
        logout(request)
        return redirect('Login-View')
    
class userProfileService:
     def getProfile():
          return
     
     def updateProfile():
          return