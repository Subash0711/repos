from user.models import (BlogUsers)
from blog_app.models import (BlogLists,UserComments)
from django.contrib.auth.hashers import make_password,check_password
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from blog_app.service import coreservices
from urllib.parse import urlencode
from user.messages import (PASSWORD_UPDATE_MSG,PASSWORD_CHECK_MSG,
DETAILS_UPDATE_MSG,USERNAME_UPDATE_MSG,USERNAME_UNAVAILABLE_MSG,
INCORRECT_USERNAME_MSG,INCORRECT_PASSWORD_MSG,CREATE_USER_SUCCESS_MSG)


class userCoreService:
    def getBlogsCount(userid):
        userBlogCounts=BlogLists.objects.filter(userid=userid).count()
        return userBlogCounts
    def getCommentsCount(userid):
        userCommentCounts=UserComments.objects.filter(user=userid).count()
        return userCommentCounts

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
            return render(request,'login.html',{'exception':INCORRECT_PASSWORD_MSG})
        else:
            return render(request,'login.html',{'exception':INCORRECT_USERNAME_MSG})
            
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
        url= reverse('Login-View')
        msg={'message': CREATE_USER_SUCCESS_MSG}
        msg=urlencode(msg)
        url+=f'?{msg}'
        return redirect(url)
        
    @classmethod
    def logoutUser(cls,request):
        logout(request)
        return redirect('Login-View')
    
class userProfileService: 
    @classmethod
    def getProfile(cls,request,userid):
        data=coreservices.getUser(userid)
        blogCount=userCoreService.getBlogsCount(userid)
        blogcmtCount=userCoreService.getCommentsCount(userid)
        title= (f"{data['userfullname']}| BlogNest")
        msg = request.GET.get('message','')
        return render (request=None,template_name='user_profile.html',context={'title':title,'userid':userid,'message':msg,'user':data,'userblogCount':blogCount,'userCmtsCount':blogcmtCount})
     
    @classmethod
    def updateUser(cls,request,userid):
        columnName=request.POST.get('column-name')
        userdata=BlogUsers.objects.get(id=userid)
        data=coreservices.getUser(userid)
        blogCount=userCoreService.getBlogsCount(userid)
        blogcmtCount=userCoreService.getCommentsCount(userid)
        if columnName == 'password-col':
            oldPassword=request.POST.get('old-password')
            newPassword=request.POST.get('new-password')
            hashedPassword=userdata.password
            if check_password(oldPassword,hashedPassword):
                encpasword=make_password(newPassword)
                userdata.password=encpasword
                userdata.save()
                url=reverse('User-Profile-View',kwargs={'userid':userid})
                msg={'message':PASSWORD_UPDATE_MSG}
                msg=urlencode(msg)
                url+=f'?{msg}'
                return redirect(url)
            msg={'errormessage':PASSWORD_CHECK_MSG,'userid':userid,'user':data,'userblogCount':blogCount,'userCmtsCount':blogcmtCount}
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
            msg={'message':DETAILS_UPDATE_MSG}
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
                msg={'message':USERNAME_UPDATE_MSG}
                msg=urlencode(msg)
                url+=f'?{msg}'
                return redirect(url)
            msg={'errormessage':USERNAME_UNAVAILABLE_MSG,'userid':userid,'user':data,'userblogCount':blogCount,'userCmtsCount':blogcmtCount}
            return render(request=None,template_name='user_profile.html',context=msg)