from django.urls import path
from . import views

urlpatterns = [
    path('Addblog/<int:userid>', views.addBlog_View,name='AddBlog_View'),
    path('Updateblog/<int:userid>/<int:blogid>', views.updateBlog_View,name='UpdateBlog_View'),
    path('DashBoard/<int:userid>', views.blogList_View,name='BlogList_View'),
    path('Searchblog/<int:userid>', views.blogList_View,name='SearchBlogLists_View'),
    path('Viewblog/<int:userid>/<int:blogid>', views.commentView,name='Blog_Comments_View'),
    path('AddComment/', views.addCommentView,name='Add_Comment_View'),
    path('ShareBlog/', views.shareBlogView,name='Share_Blog_View'),
    path('DeleteComment', views.deleteCommentView,name='BlogComment_delete_View'),
    path('UpdateComment', views.updateCommentView,name='BlogComment_update_View'),
    path('clear',views.clearMessage,name='clear_view'),
    path('like/<int:userid>/<int:blogid>',views.likeBlogsView,name='Blog_like_view')
]