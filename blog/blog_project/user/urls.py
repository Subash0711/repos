from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('Signup', views.signup_View,name='Signup-View'),
    path('Login', views.login_View,name='Login-View'),
    path('Logout',views.logout_view,name='Logout-View'),
    path('User/Profile/<int:userid>',views.user_Profile_View,name='User-Profile-View'),
    path('api/token',TokenObtainPairView.as_view(),name='Token_obtain_view')
]