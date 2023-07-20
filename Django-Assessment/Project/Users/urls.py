from django.urls import path
from . import views

urlpatterns =[
    path('registration/',views.userRegistration_view,name='User Resgistration'),
    path('login/',views.userLogin_view,name='User Login')
]