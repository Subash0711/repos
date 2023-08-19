from django.shortcuts import render
from rest_framework.views  import APIView
from core.services import (
CityServices,EducationlevelServices,EducationqualificationServices,EducationspecializationServices,
EmployeedirectoryServices,EventdetailsServices,ExperiencelevelServices,GenderServices,MaritalstatusServices,JobrequisitionServices,
PersonaServices,ReasonforchangeServices,ScreeningmodeServices,SourceServices,SourcetypeServices
)
# Create your views here.
class CityViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return CityServices.getCity(id)
        elif id is None:
            return CityServices.getAll()
    def post(self,request):
        method='POST'
        return CityServices.create_or_Update_City(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return CityServices.create_or_Update_City(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return CityServices.deleteCity(id)
    
class EducationlevelViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return EducationlevelServices.getEducationlevel(id)
        elif id is None:
            return EducationlevelServices.getAll()
    def post(self,request):
        method='POST'
        return EducationlevelServices.create_or_Update_Educationlevel(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return EducationlevelServices.create_or_Update_Educationlevel(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return EducationlevelServices.deleteEducationlevel(id)

class EducationqualificationViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return EducationqualificationServices.getEducationqualification(id)
        elif id is None:
            return EducationqualificationServices.getAll()
    def post(self,request):
        method='POST'
        return EducationqualificationServices.create_or_Update_Educationqualification(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return EducationqualificationServices.create_or_Update_Educationqualification(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return EducationqualificationServices.deleteEducationqualification(id)

class EducationspecializationViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return EducationspecializationServices.getEducationspecialization(id)
        elif id is None:
            return EducationspecializationServices.getAll()
    def post(self,request):
        method='POST'
        return EducationspecializationServices.create_or_Update_Educationspecialization(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return EducationspecializationServices.create_or_Update_Educationspecialization(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return EducationspecializationServices.deleteEducationspecialization(id)

class EmployeedirectoryViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return EmployeedirectoryServices.getEmployeedirectory(id)
        elif id is None:
            return EmployeedirectoryServices.getAll()
    def post(self,request):
        method='POST'
        return EmployeedirectoryServices.create_or_Update_Employeedirectory(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return EmployeedirectoryServices.create_or_Update_Employeedirectory(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return EmployeedirectoryServices.deleteEmployeedirectory(id)
    
class EventdetailsViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return EventdetailsServices.getEventdetails(id)
        elif id is None:
            return EventdetailsServices.getAll()
    def post(self,request):
        method='POST'
        return EventdetailsServices.create_or_Update_Eventdetails(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return EventdetailsServices.create_or_Update_Eventdetails(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return EventdetailsServices.deleteEventdetails(id)
    
class ExperiencelevelViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return ExperiencelevelServices.getExperiencelevel(id)
        elif id is None:
            return ExperiencelevelServices.getAll()
    def post(self,request):
        method='POST'
        return ExperiencelevelServices.create_or_Update_Experiencelevel(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return ExperiencelevelServices.create_or_Update_Experiencelevel(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return ExperiencelevelServices.deleteExperiencelevel(id)
    
class GenderViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return GenderServices.getGender(id)
        elif id is None:
            return GenderServices.getAll()
    def post(self,request):
        method='POST'
        return GenderServices.create_or_Update_Gender(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return GenderServices.create_or_Update_Gender(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return GenderServices.deleteGender(id)    

class MaritalstatusViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return MaritalstatusServices.getMaritalstatus(id)
        elif id is None:
            return MaritalstatusServices.getAll()
    def post(self,request):
        method='POST'
        return MaritalstatusServices.create_or_Update_Maritalstatus(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return MaritalstatusServices.create_or_Update_Maritalstatus(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return MaritalstatusServices.deleteMaritalstatus(id)
    
class JobrequisitionViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return JobrequisitionServices.getJobrequisition(id)
        elif id is None:
            return JobrequisitionServices.getAll()
    def post(self,request):
        method='POST'
        return JobrequisitionServices.create_or_Update_Jobrequisition(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return JobrequisitionServices.create_or_Update_Jobrequisition(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return JobrequisitionServices.deleteJobrequisition(id)

class PersonaViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return PersonaServices.getPersona(id)
        elif id is None:
            return PersonaServices.getAll()
    def post(self,request):
        method='POST'
        return PersonaServices.create_or_Update_Persona(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return PersonaServices.create_or_Update_Persona(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return PersonaServices.deletePersona(id)

class ReasonforchangeViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return ReasonforchangeServices.getReasonforchange(id)
        elif id is None:
            return ReasonforchangeServices.getAll()
    def post(self,request):
        method='POST'
        return ReasonforchangeServices.create_or_Update_Reasonforchange(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return ReasonforchangeServices.create_or_Update_Reasonforchange(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return ReasonforchangeServices.deleteReasonforchange(id)
    
class ScreeningmodeViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return ScreeningmodeServices.getScreeningmode(id)
        elif id is None:
            return ScreeningmodeServices.getAll()
    def post(self,request):
        method='POST'
        return ScreeningmodeServices.create_or_Update_Screeningmode(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return ScreeningmodeServices.create_or_Update_Screeningmode(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return ScreeningmodeServices.deleteScreeningmode(id)
    
class SourceViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return SourceServices.getSource(id)
        elif id is None:
            return SourceServices.getAll()
    def post(self,request):
        method='POST'
        return SourceServices.create_or_Update_Source(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return SourceServices.create_or_Update_Source(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return SourceServices.deleteSource(id)

class SourcetypeViews(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id:
            return SourcetypeServices.getSourcetype(id)
        elif id is None:
            return SourcetypeServices.getAll()
    def post(self,request):
        method='POST'
        return SourcetypeServices.create_or_Update_Sourcetype(request,method)
    
    def put(self,request):
        id = request.query_params.get('id')
        method='PUT'
        return SourcetypeServices.create_or_Update_Sourcetype(request,method,id)
    
    def delete(self,request):
        id = request.query_params.get('id')
        return SourcetypeServices.deleteSourcetype(id)
