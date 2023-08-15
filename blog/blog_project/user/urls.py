from django.urls import path
from user.views import (
    signup_View,login_View,logout_view,home_View,user_Profile_View
)
urlpatterns = [
    path('signup/', signup_View,name='Signup-View'),
    path('login/', login_View,name='Login-View'),
    path('logout',logout_view,name='Logout-View'),
    path('user/profile/<int:userid>',user_Profile_View,name='User-Profile-View')
]