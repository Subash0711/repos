from django.urls import path
from blog_app.views import (
    blogList_View,
    addBlog_View,updateBlog_View,
    commentView,addCommentView,shareBlogView
    )

# handler404=custom_errors

urlpatterns = [
    path('Addblog/<int:userid>', addBlog_View,name='AddBlog-View'),
    path('Updateblog/<int:userid>/<int:blogid>', updateBlog_View,name='UpdateBlog-View'),
    path('DashBoard/<int:userid>',blogList_View,name='BlogList_View'),
    path('Viewblog/<int:userid>/<int:blogid>',commentView,name='Blog-Comment_View'),
    path('AddComment/',addCommentView,name='Add-Comment-View'),
    path('ShareBlog/',shareBlogView,name='Share-Blog-View'),
]