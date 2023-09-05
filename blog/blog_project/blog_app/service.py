from django.db.models import F
from blog_app.models import (BlogLists,UserComments)
from user.models import (BlogUsers)
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.urls import reverse
from urllib.parse import urlencode
from django.core.paginator import Paginator
from . import messages 
from django.http import HttpResponse

class coreservices:
    @staticmethod
    def clearMessage(request):
        if 'message' in request.session:
            del request.session['message']
        return HttpResponse()
    
    @staticmethod
    def getUser(id):
        user=BlogUsers.objects.get(id=id)
        return {'userfullname':user.fullname,'username':user.username,'usermail':user.emailid,'userMobileNo':user.mobile_no,'userid':user.id,'usergender':user.gender}
    @staticmethod
    def getBlog(id):
        blog=BlogLists.objects.get(blog_id=id)
        return {'blog_id':blog.blog_id,'blog_title':blog.blog_title,'blog_content':blog.blog_content,'blog_userid':blog.userid}


class blogCoreService:
    def getBlogsCount(userid):
        userBlogCounts=BlogLists.objects.filter(userid=userid).count()
        return userBlogCounts
    def getCommentsCount(userid):
        userCommentCounts=UserComments.objects.filter(user=userid).count()
        return userCommentCounts

class BlogListServices:
        @classmethod
        def getAllBlog(cls,request,userid):
            blog_data=BlogLists.objects.select_related('userid').values(
                 'blog_id','userid__fullname','userid','blog_title','blog_content','created_at','isUpdate'
            ).order_by('-blog_id')
            userdata=coreservices.getUser(userid)
            item_per_page=5
            title='Feed | BlogNest'
            paginator=Paginator(blog_data,item_per_page)
            page_number=request.GET.get('page')
            page=paginator.get_page(page_number)
            msg = request.session.get('message')
            ctxData={'bloglists':page,
                     'user':userdata['userfullname'],
                     'usermail':userdata['usermail'],
                     'userid':userid,'message':msg,
                     'title':title}
            return render(request=None,template_name='blog_lists.html',context=ctxData)
        
        @classmethod
        def addBlog(cls,request,userId):
            title=request.POST.get('blog_title')
            content=request.POST.get('blog_content')
            blog_user = BlogUsers.objects.get(id=userId)
            data=BlogLists(blog_title=title,blog_content=content,userid=blog_user)
            data.save()
            url=reverse('BlogList_View',kwargs={'userid':userId})
            request.session['message'] = messages.ADD_BLOG_MESSAGE
            return redirect(url)
        
        @classmethod
        def updateBlog(cls,request,userId,blogid):
            title=request.POST.get('blog_title')
            content=request.POST.get('blog_content')
            existBlogData=BlogLists.objects.get(blog_id=blogid)
            existBlogData.blog_title=title
            existBlogData.blog_content=content
            existBlogData.isUpdate = True
            existBlogData.save()
            url=reverse('Blog_Comments_View',kwargs={'userid':userId,'blogid':blogid})
            request.session['message'] = messages.BLOG_UPDATE_MSG
            return redirect(url)

class BlogCommentServices:  
        @classmethod
        def BlogComments(cls,request,blogid,userid):
            blogCtx=BlogLists.objects.select_related('userid').filter(blog_id=blogid).values(
                 'userid','blog_id','userid__fullname','blog_title','blog_content','created_at','isUpdate'
            ).order_by('-blog_id')
                    
            userdata=coreservices.getUser(userid)
            title='Post | Blog | BlogNest'
            msg = request.session.get('message')
            cmtdata=UserComments.objects.select_related('blog','user').filter(is_deleted=False,blog=blogid).prefetch_related('blog__userid').order_by('-cmt_id')
            return render(request,'view_blog.html',
                          {'cmtCtx':cmtdata,
                           'bloglist':blogCtx,
                           'message':msg,
                           'user':userdata['userfullname'],
                           'usermail':userdata['usermail'],
                           'userid':userid,
                           'title':title})
        
        @classmethod
        def addBlogComment(cls,request):
            blogid=request.POST.get('blogId')
            userid=request.POST.get('userId')
            id=request.POST.get('Page-id')
            CmtCont=request.POST.get('user_comment')
            blog_instances=BlogLists.objects.get(blog_id=blogid)
            user_instances=BlogUsers.objects.get(id=userid)
            data=UserComments(blog=blog_instances,cmt_content=CmtCont,user=user_instances)
            data.save()
            if int(id) == 0:
                url=reverse('BlogList_View',kwargs={'userid':userid})
                request.session['message'] = messages.ADD_COMMENT_MESSAGE
                return redirect(url)
            elif int(id) == 1:
                url=reverse('Blog_Comments_View',kwargs={'userid':userid,'blogid':blogid})
                request.session['message'] = messages.ADD_COMMENT_MESSAGE
                return redirect(url)
            
        @classmethod
        def deleteBlogComments(cls,request):
            blogId=request.POST.get('blogid')
            userid=request.POST.get('userid')
            commentid=request.POST.get('deleteCommentId')
            cmtdata=UserComments.objects.get(cmt_id=commentid)
            cmtdata.is_deleted=True
            cmtdata.save()
            url=reverse('Blog_Comments_View',kwargs={'userid':userid,'blogid':blogId})
            request.session['message'] = messages.BLOG_CMT_DELETE_MSG
            return redirect(url)

        @classmethod
        def updateBlogComments(cls,request):
            blogId=request.POST.get('blogid')
            userid=request.POST.get('userid')
            commentid=request.POST.get('editCommentId')
            updatecomment=request.POST.get('update_comment')
            cmtdata=UserComments.objects.get(cmt_id=commentid)
            cmtdata.cmt_content=updatecomment
            cmtdata.isUpdate=True
            cmtdata.save()
            url=reverse('Blog_Comments_View',kwargs={'userid':userid,'blogid':blogId})
            request.session['message'] = messages.BLOG_CMT_UPDATE_MSG
            return redirect(url)
        
class BlogShareServices:
     def shareBlog(request):
        blogId=request.POST.get('blogid')
        userid=(request.POST.get('userid'))
        id=int(request.POST.get('pageId'))
        receive_mail=request.POST.get('receiverMail')
        userdata=coreservices.getUser(userid)
        blog_data=BlogLists.objects.filter(blog_id=blogId).values('blog_id','blog_title','blog_content','userid__fullname').annotate(fullname=F('userid__fullname')).first()
        subject=f"Check Out This Blog: {blog_data['blog_title']}"
        emailCnt = render_to_string('email_share.html',{'blog':blog_data,'sender':userdata['userfullname']})
        email= EmailMessage(subject,emailCnt,to=[receive_mail])
        email.content_subtype='html'
        email.send()
        if id == 0:
            url=reverse('BlogList_View',kwargs={'userid':int(userid)})
        elif id == 1:
            url=reverse('Blog_Comments_View',kwargs={'userid':userid,'blogid':blogId})
        request.session['message'] = messages.BLOG_SHARED_MESSAGE
        return redirect(url)