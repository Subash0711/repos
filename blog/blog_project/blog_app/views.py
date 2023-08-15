from django.shortcuts import render,redirect
from blog_app.service import (BlogListServices,BlogCommentServices,BlogShareServices)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from blog_app.service import getUser
    

def blogList_View(request,userid):
    return BlogListServices.getAllBlog(request,userid)

@csrf_exempt
def addBlog_View(request,userid):
    if request.method == 'POST':
        return BlogListServices.addBlog(request,userid)
    if request.method == 'GET':
        userdata=getUser(userid)
        contx={
            'userid':int(userid),
            'user':userdata['userfullname'],
            'title':'Post | BlogNest'
        }
        return render (request=None,template_name='add_blog.html',context=contx)

def commentView(request,blogid,user):
    return BlogCommentServices.BlogComments(request,blogid,user)

@csrf_exempt
def addCommentView(request,id):
    return BlogCommentServices.addBlogComment(request,id)

@csrf_exempt
def shareBlogView(request):
    if request.method == 'POST':
        return BlogShareServices.shareBlog(request)
        