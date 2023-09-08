from django.urls import path
from . import views

urlpatterns = [
    path('Signup', views.signup_View,name='Signup-View'),
    path('Login', views.login_View,name='Login-View'),
    path('Logout',views.logout_view,name='Logout-View'),
    path('User/Profile/<int:userid>',views.user_Profile_View,name='User-Profile-View'),
    path('usernameavailbilty',views.availablityUsername,name='UsernameAvailable'),
    path('emailavailbilty',views.availablitymail,name='emailAvailable')
]