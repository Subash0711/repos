from django.urls import path
from blog_app.views import (login_View,signup_View,home_View,blogList_View)
urlpatterns = [
    path('login/', login_View,name='Login-View'),
    path('signup/', signup_View,name='Signup-View'),
    path('', home_View,name='Home-View'),
    path('DashBoard/<int:userid>',blogList_View,name='BlogList_View')
]