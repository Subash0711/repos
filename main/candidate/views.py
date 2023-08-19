from rest_framework.views  import APIView
from  rest_framework.response import Response
from rest_framework import status
from candidate.service import (
PersonalDetailsServices,ApplicationDetailsServices,EducationDetailsServices,CandidateLoginDetailsServices,
WorkDetailsServices,CoreServices
)   
class PersonalDetailsView(APIView):

    def get(self,request):
        id = request.query_params.get('id')
        return PersonalDetailsServices.get_personal_details(id)

    def post(self,request):
        return PersonalDetailsServices.create_personal_details(request)
        
    def put(self,request):
        id = request.query_params.get('id')
        return PersonalDetailsServices.update_personal_details(request,id)
    
class EducationDetailsView(APIView):
    def get(self,request,id):
        return EducationDetailsServices.get_Education_details(id)
    
    def post(self,request,id):
        method='POST'
        return EducationDetailsServices.create_or_update_Education_details(request,id,method)
    
    def put(self,request,id):
        method='PUT'
        return EducationDetailsServices.create_or_update_Education_details(request,id,method)
        
class WorkDetailsView(APIView):
    def get(self,request,id):
        return WorkDetailsServices.get_work_details(id)
    
    def post(self,request,id):
        method='POST'
        return WorkDetailsServices.create_or_update_work_details(request,id,method)
    
    def put(self,request,id):
        method='PUT'
        return WorkDetailsServices.create_or_update_work_details(request,id,method)
    
class ApplicationDetailsView(APIView):
    def get(self,request,id):
        return ApplicationDetailsServices.get_Application_details(id)
    
    def post(self,request,id):
        method='POST'
        return ApplicationDetailsServices.create_or_update_Application_details(request,id,method)
    
    def put(self,request,id):
        method='PUT'
        return ApplicationDetailsServices.create_or_update_Application_details(request,id,method)
    
class LoginDetailsView(APIView):
    def get(self,request,id):
        return CandidateLoginDetailsServices.get_login_details(id)
    
    def post(self,request,id):
        method='POST'
        return CandidateLoginDetailsServices.create_or_update_login_details(request,id,method)
    
    def put(self,request,id):
        method='PUT'
        return CandidateLoginDetailsServices.create_or_update_login_details(request,id,method)
    
class DeleteProfileView(APIView):
    def delete(self,request,id):
        return CoreServices.deleteprofile(id)

