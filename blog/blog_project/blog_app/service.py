import datetime
from blog_app.models import (BlogLists,BlogUsers,UserComments)
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode,parse_qs
from django.contrib import messages
from django.contrib.auth import logout
from django.core.paginator import Paginator

def getUser(id):
    user=BlogUsers.objects.get(id=id)
    return {'userfullname':user.fullname,'username':user.username,'usermail':user.emailid,'userMobileNo':user.mobile_no,'userid':user.id}

def getBlog(id):
    blog=BlogLists.objects.get(blog_id=id)
    return {'blog_id':blog.blog_id,'blog_title':blog.blog_title,'blog_content':blog.blog_content}


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
        return redirect('Login-View')
        
    @classmethod
    def logoutUser(cls,request):
        logout(request)
        return redirect('Login-View')

class BlogListServices:
        @classmethod
        def getAllBlog(cls,request,userid):
            blog_data=BlogLists.objects.select_related('userid').values(
                 'blog_id','userid__fullname','userid','blog_title','blog_content','created_at'
            ).order_by('-blog_id')
            userdata=getUser(userid)
            item_per_page=5
            title='Feed | Digital Diary'
            paginator=Paginator(blog_data,item_per_page)
            page_number=request.GET.get('page')
            page=paginator.get_page(page_number)
            queryParams=parse_qs(request.META['QUERY_STRING'])
            msg=queryParams.get('message',[''])[0]
            ctxData={'bloglists':page,'user':userdata['userfullname'],'usermail':userdata['usermail'],'userid':userid,'status':msg,'loginUserId':userdata['userid'],'title':title}
            return render(request=None,template_name='blog_lists.html',context=ctxData)
        
        @classmethod
        def addBlog(cls,request,userId):
            title=request.POST.get('blog_title')
            content=request.POST.get('blog_content')
            blog_user = BlogUsers.objects.get(id=userId)
            data=BlogLists(blog_title=title,blog_content=content,userid=blog_user)
            data.save()
            url=reverse('BlogList_View',kwargs={'userid':userId})
            msg={'message':'Your Blog Added Successfully'}
            msg=urlencode(msg)
            url+=f"?{msg}"
            return redirect(url)

class BlogCommentServices:  
            
        @classmethod
        def BlogComments(cls,request,blogid,userid):
            blogCtx=BlogLists.objects.select_related('userid').filter(blog_id=blogid).values(
                 'userid','blog_id','userid__fullname','blog_title','blog_content','created_at'
            ).order_by('-blog_id')
            userdata=getUser(userid)
            title='Post | Blog | Digital Diary'
            queryParams=parse_qs(request.META['QUERY_STRING'])
            msg=queryParams.get('message',[''])[0]
            cmtdata=UserComments.objects.select_related('blog','user').filter(is_deleted=False,blog=blogid).prefetch_related('blog__userid').order_by('-cmt_id')
            return render(request,'view_blog.html',{'cmtCtx':cmtdata,'bloglist':blogCtx,'status':msg,'user':userdata['userfullname'],'usermail':userdata['usermail'],'loginUserId':userdata['userid'],'title':title})
        
        @classmethod
        def addBlogComment(cls,request,id):
            blogid=request.POST.get('blogId')
            userid=request.POST.get('userId')
            CmtCont=request.POST.get('user_comment')
            blog_instances=BlogLists.objects.get(blog_id=blogid)
            user_instances=BlogUsers.objects.get(id=userid)
            data=UserComments(blog=blog_instances,cmt_content=CmtCont,user=user_instances)
            data.save()
            if id == 0:
                url=reverse('BlogList_View',kwargs={'userid':userid})
            elif id == 1:
                 url=reverse('Blog-Comment_View',kwargs={'user':userid,'blogid':blogid})
            msg={'message':'Your Comment Addded Sucessfully'}
            msg=urlencode(msg)
            url+=f'?{msg}'
            return redirect(url)