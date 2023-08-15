from django.urls import path
from blog_app.views import (
    blogList_View,
    addBlog_View,
    commentView,addCommentView,shareBlogView
    )
urlpatterns = [
    path('addblog/<int:userid>', addBlog_View,name='AddBlog-View'),
    path('DashBoard/<int:userid>',blogList_View,name='BlogList_View'),
    path('viewblog/<int:user>/<int:blogid>',commentView,name='Blog-Comment_View'),
    path('addComment/<int:id>',addCommentView,name='Add-Comment-View'),
    path('shareBlog/',shareBlogView,name='Share-Blog-View') 
]