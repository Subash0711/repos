from candidate.views import (ApplicationDetailsView,PersonalDetailsView,
EducationDetailsView,WorkDetailsView,ApplicationDetailsView,LoginDetailsView,DeleteProfileView)
from django.urls import path

urlpatterns = [
    # For post =http://127.0.0.1:8000/api/v1/{}/
    # For Get,put,delete =http://127.0.0.1:8000/api/v1/{}/?id=0
    path('personal',PersonalDetailsView.as_view(),name='Personal_Details_View'),
    path('education/<int:id>',EducationDetailsView.as_view(),name='Education_Details_View'),
    path('experiance/<int:id>',WorkDetailsView.as_view(),name='Work_Details_View'),
    path('application/<int:id>',ApplicationDetailsView.as_view(),name='Application_Details_View'),
    path('login/<int:id>',LoginDetailsView.as_view(),name='Login_Details_View'),
    path('delete/<int:id>',DeleteProfileView.as_view(),name='Delete_Profile_View'),
] 