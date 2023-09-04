from django.urls import path
from blog_app.views import (
    blogList_View,
    addBlog_View,updateBlog_View,
    commentView,addCommentView,shareBlogView,deleteCommentView,updateCommentView
    )

# handler404=custom_errors

urlpatterns = [
    path('Addblog/<int:userid>', addBlog_View,name='AddBlog_View'),
    path('Updateblog/<int:userid>/<int:blogid>', updateBlog_View,name='UpdateBlog_View'),
    path('DashBoard/<int:userid>',blogList_View,name='BlogList_View'),
    path('Viewblog/<int:userid>/<int:blogid>',commentView,name='Blog_Comments_View'),
    path('AddComment/',addCommentView,name='Add_Comment_View'),
    path('ShareBlog/',shareBlogView,name='Share_Blog_View'),
    path('DeleteComment',deleteCommentView,name='BlogComment_delete_View'),
    path('UpdateComment',updateCommentView,name='BlogComment_update_View'),
]