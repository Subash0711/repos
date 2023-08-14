from django.urls import path
from blog_app.views import (
    login_View,signup_View,home_View,blogList_View,addBlog_View,logout_view,commentView,addCommentView,shareBlogView
    )
urlpatterns = [
    path('login/', login_View,name='Login-View'),
    path('signup/', signup_View,name='Signup-View'),
    path('addblog/<int:userid>', addBlog_View,name='AddBlog-View'),
    path('', home_View,name='Home-View'),
    path('DashBoard/<int:userid>',blogList_View,name='BlogList_View'),
    path('logout',logout_view,name='Logout-View'),
    path('viewblog/<int:user>/<int:blogid>',commentView,name='Blog-Comment_View'),
    path('addComment/<int:id>',addCommentView,name='Add-Comment-View'),
    path('shareBlog/',shareBlogView,name='Share-Blog-View') 
]