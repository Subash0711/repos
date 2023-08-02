from blog_app.models import (BlogLists,BlogUsers)
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

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
        print(request)
        fullname=request.POST.get('full_name')
        emailId=request.POST.get('email_address')
        username=request.POST.get('user_name')
        phonenumber=request.POST.get('phone_number')
        password=request.POST.get('user_password')
        encPassword=make_password(password=password)

        data=BlogUsers(fullname=fullname,emailid=emailId,username=username,mobile_no=phonenumber,password=encPassword)
        data.save()
        return render(request=None,template_name='login.html')
    

class BlogListServices:
        @classmethod
        def getAllBlog(cls,request,userid):
            blog_data=BlogLists.objects.select_related('userid').values(
                 'blog_id','userid__fullname','blog_title','blog_content','created_at'
            ).order_by('-created_at')
            user=BlogUsers.objects.get(id=userid)
            username = user.fullname
            usermail = user.emailid
            ctxData={'bloglists':blog_data,'user':username,'usermail':usermail}
            return render(request=None,template_name='blog_lists.html',context=ctxData)
        