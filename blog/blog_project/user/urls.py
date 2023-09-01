from django.urls import path
from user.views import (
    signup_View,login_View,logout_view,user_Profile_View
)
urlpatterns = [
    path('Signup', signup_View,name='Signup-View'),
    path('Login', login_View,name='Login-View'),
    path('Logout',logout_view,name='Logout-View'),
    path('User/Profile/<int:userid>',user_Profile_View,name='User-Profile-View'),
]