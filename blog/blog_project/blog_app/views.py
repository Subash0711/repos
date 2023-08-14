from django.shortcuts import render,redirect
from django.views import View
from blog_app.service import (userLoginService,BlogListServices,BlogCommentServices,BlogShareServices)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from blog_app.models import (BlogLists,BlogUsers,UserComments)

@csrf_exempt
def login_View(request):
    if request.method == 'POST':
        return userLoginService.userAuthentication(request)
    elif request.method == 'GET':
        title='Digital Diary : Login '
        return render (request=None,template_name='login.html',context={'title':title})
    
@csrf_exempt
def  signup_View(request):
    if request.method == 'POST':
        return userLoginService.adduser(request=request)
    elif request.method == 'GET':
        title='Digital Diary : Sign Up '
        return render (request=None,template_name='signup.html',context={'title':title})
    
def home_View(request):
    return redirect ('Login-View')

def blogList_View(request,userid):
    return BlogListServices.getAllBlog(request,userid)

@csrf_exempt
def addBlog_View(request,userid):
    if request.method == 'POST':
        return BlogListServices.addBlog(request,userid)
    if request.method == 'GET':
        contx={
            'userid':int(userid)
        }
        return render (request=None,template_name='add_blog.html',context=contx)

def logout_view(request):
    return userLoginService.logoutUser(request)

def commentView(request,blogid,user):
    return BlogCommentServices.BlogComments(request,blogid,user)

@csrf_exempt
def addCommentView(request,id):
    return BlogCommentServices.addBlogComment(request,id)

@csrf_exempt
def shareBlogView(request):
    if request.method == 'POST':
        return BlogShareServices.shareBlog(request)
        