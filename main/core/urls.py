from core.views import (CityViews,EducationlevelViews,
EducationqualificationViews,EducationspecializationViews,EmployeedirectoryViews,EventdetailsViews,ExperiencelevelViews,GenderViews,
JobrequisitionViews,MaritalstatusViews,PersonaViews,ReasonforchangeViews,ScreeningmodeViews,SourcetypeViews,SourceViews
)
from django.urls import path

urlpatterns = [
    # For post =http://127.0.0.1:8000/api/v1/apiname
    # For Get,put,delete =http://127.0.0.1:8000/api/v1/apiname?id=0
    path('city',CityViews.as_view(),name='City_View'),
    path('educationlevel',EducationlevelViews.as_view(),name='Educationlevel_View'),
    path('qualification',EducationqualificationViews.as_view(),name='EducationQualification_View'),
    path('specialization',EducationspecializationViews.as_view(),name='EducationSpecializtion_View'),
    path('directory',EmployeedirectoryViews.as_view(),name='EmployeeDirectory_View'),
    path('event',EventdetailsViews.as_view(),name='EventDetails_View'),
    path('experiencelevel',ExperiencelevelViews.as_view(),name='ExperienceLevel_Views'),
    path('gender',GenderViews.as_view(),name='Gender_View'),
    path('requisition',JobrequisitionViews.as_view(),name='JobRequestion_View'),
    path('maritalstatus',MaritalstatusViews.as_view(),name='MartialStatus_View'),
    path('persona',PersonaViews.as_view(),name='Persona_View'),
    path('reasonforchange',ReasonforchangeViews.as_view(),name='ReasonForChange_View'),
    path('mode',ScreeningmodeViews.as_view(),name='ScreeingMode_View'),
    path('source',SourceViews.as_view(),name='Source_View'),
    path('sourcetype',SourcetypeViews.as_view(),name='SourceType_View'),
] 