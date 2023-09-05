from django.shortcuts import render,redirect
from blog_app.service import (BlogListServices,BlogCommentServices,BlogShareServices,BlogLikeService)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from blog_app.service import coreservices
from user.service import TokenService


@TokenService.validateToken
def blogList_View(request,userid):
    access_token = request.session.get('access_token')
    return BlogListServices.getAllBlog(request,userid)

@csrf_exempt
@TokenService.validateToken
def addBlog_View(request,userid):
    if request.method == 'POST':
        return BlogListServices.addBlog(request,userid)
    if request.method == 'GET':
        userdata=coreservices.getUser(userid)
        contx={
            'userid':int(userid),
            'user':userdata['userfullname'],
            'title':'Post | BlogNest',
            'headline':'What you want talk about?',
            'method':'Add'
        }
        return render (request=None,template_name='add_or_update_blog.html',context=contx)

@csrf_exempt
@TokenService.validateToken
def updateBlog_View(request,userid,blogid):
    if request.method == 'POST':
        return BlogListServices.updateBlog(request,userid,blogid)
    if request.method == 'GET':
        blogdata=coreservices.getBlog(blogid)
        userdata=coreservices.getUser(userid)
        contx={
            'userid':int(userid),
            'blogid':int(blogid),
            'user':userdata['userfullname'],
            'title':'Update | BlogNest',
            'blogdata':blogdata,
            'method':'Update',
            'headline':'You have anything better!',
        }
        return render (request=None,template_name='add_or_update_blog.html',context=contx)

@TokenService.validateToken    
def commentView(request,blogid,userid):
    return BlogCommentServices.BlogComments(request,blogid,userid)

@csrf_exempt
@TokenService.validateToken
def addCommentView(request):
    return BlogCommentServices.addBlogComment(request)

@csrf_exempt
@TokenService.validateToken
def shareBlogView(request):
    if request.method == 'POST':
        return BlogShareServices.shareBlog(request)

@csrf_exempt
@TokenService.validateToken
def deleteCommentView(request):
    return BlogCommentServices.deleteBlogComments(request)  

@csrf_exempt
@TokenService.validateToken
def updateCommentView(request):
    return BlogCommentServices.updateBlogComments(request)

def clearMessage(request):
    return coreservices.clearMessage(request)

def likeBlogsView(request,userid,blogid):
    return BlogLikeService.addlike(request,userid,blogid)