from django.shortcuts import render,redirect
from blog_app.service import (BlogListServices,BlogCommentServices,BlogShareServices)
from django.views.decorators.csrf import csrf_exempt
from blog_app.service import coreservices

def blogList_View(request,userid):
    return BlogListServices.getAllBlog(request,userid)

@csrf_exempt
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
    
def commentView(request,blogid,userid):
    return BlogCommentServices.BlogComments(request,blogid,userid)

@csrf_exempt
def addCommentView(request):
    return BlogCommentServices.addBlogComment(request)

@csrf_exempt
def shareBlogView(request):
    if request.method == 'POST':
        return BlogShareServices.shareBlog(request)

@csrf_exempt
def deleteCommentView(request):
    return BlogCommentServices.deleteBlogComments(request)  
@csrf_exempt
def updateCommentView(request):
    return BlogCommentServices.updateBlogComments(request)