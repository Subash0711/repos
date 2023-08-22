from rest_framework.response import Response
from core.models import (City, Educationlevel, Educationqualification,
Educationspecialization, Employeedirectory, Eventdetails,Experiencelevel, Gender, Jobrequisition, Maritalstatus,
Persona, Reasonforchange, Screeningmode, Source, Sourcetype)
from core.serializer import (CitySerializer, EducationlevelSerializer, EducationqualificationSerializer,EducationspecializationSerializer, 
EmployeedirectorySerializer, EventdetailsSerializer,ExperiencelevelSerializer, GenderSerializer, JobrequisitionSerializer, MaritalstatusSerializer,
PersonaSerializer,ReasonforchangeSerializer, ScreeningmodeSerializer,SourceSerializer, SourcetypeSerializer )
from rest_framework import status

class CityServices:
    def getAll():
        instances=City.objects.all()
        serialize=CitySerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getCity(id):
        instances=City.objects.filter(id=id).first()
        if instances:
            serializer=CitySerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'City Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_City(request,method,id=None):
        instances=City.objects.filter(id=id).first()
        serialize_data=CitySerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'City Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=CitySerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'City Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'City Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteCity(id):
        instances=City.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'User Profile Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'City Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
class EducationlevelServices:
    def getAll():
        instances=Educationlevel.objects.all()
        serialize=EducationlevelSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getEducationlevel(id):
        instances=Educationlevel.objects.filter(id=id).first()
        if instances:
            serializer=EducationlevelSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Educationlevel Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Educationlevel(request,method,id=None):
        instances=Educationlevel.objects.filter(id=id).first()
        serialize_data=EducationlevelSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Educationlevel Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        if method == 'PUT' and instances:
            serializer=EducationlevelSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Educationlevel Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Educationlevel Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteEducationlevel(id):
        instances=Educationlevel.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Educationlevel Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Educationlevel Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
class EducationqualificationServices:
    def getAll():
        instances=Educationqualification.objects.all()
        serialize=EducationqualificationSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getEducationqualification(id):
        instances=Educationqualification.objects.filter(id=id).first()
        if instances:
            serializer=EducationqualificationSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Educationqualification Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Educationqualification(request,method,id=None):
        instances=Educationqualification.objects.filter(id=id).first()
        serialize_data=EducationqualificationSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Educationqualification Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=EducationqualificationSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Educationqualification Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Educationqualification Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteEducationqualification(id):
        instances=Educationqualification.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Educationqualification Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Educationqualification Details not found'}, status=status.HTTP_404_NOT_FOUND)

class EducationspecializationServices:
    def getAll():
        instances=Educationspecialization.objects.all()
        serialize=EducationspecializationSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getEducationspecialization(id):
        instances=Educationspecialization.objects.filter(id=id).first()
        if instances:
            serializer=EducationspecializationSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Educationspecialization Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Educationspecialization(request,method,id=None):
        instances=Educationspecialization.objects.filter(id=id).first()
        serialize_data=EducationspecializationSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Educationspecialization Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=EducationspecializationSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Educationspecialization Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Educationspecialization Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteEducationspecialization(id):
        instances=Educationspecialization.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Educationspecialization Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Educationspecialization Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
class EmployeedirectoryServices:
    def getAll():
        instances=Employeedirectory.objects.all()
        serialize=EmployeedirectorySerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getEmployeedirectory(id):
        instances=Employeedirectory.objects.filter(id=id).first()
        if instances:
            serializer=EmployeedirectorySerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Employeedirectory Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Employeedirectory(request,method,id=None):
        instances=Employeedirectory.objects.filter(id=id).first()
        serialize_data=EmployeedirectorySerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Employeedirectory Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=EmployeedirectorySerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Employeedirectory Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Employeedirectory Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteEmployeedirectory(id):
        instances=Employeedirectory.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Employeedirectory Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Employeedirectory Details not found'}, status=status.HTTP_404_NOT_FOUND)

class EventdetailsServices:
    def getAll():
        instances=Eventdetails.objects.all()
        serialize=EventdetailsSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getEventdetails(id):
        instances=Eventdetails.objects.filter(id=id).first()
        if instances:
            serializer=EventdetailsSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Eventdetails Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Eventdetails(request,method,id=None):
        instances=Eventdetails.objects.filter(id=id).first()
        serialize_data=EventdetailsSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Eventdetails Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=EventdetailsSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Eventdetails Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Eventdetails Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteEventdetails(id):
        instances=Eventdetails.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Eventdetails Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Eventdetails Details not found'}, status=status.HTTP_404_NOT_FOUND)

class ExperiencelevelServices:
    def getAll():
        instances=Experiencelevel.objects.all()
        serialize=ExperiencelevelSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getExperiencelevel(id):
        instances=Experiencelevel.objects.filter(id=id).first()
        if instances:
            serializer=ExperiencelevelSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Experiencelevel Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Experiencelevel(request,method,id=None):
        instances=Experiencelevel.objects.filter(id=id).first()
        serialize_data=ExperiencelevelSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Experiencelevel Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=ExperiencelevelSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Experiencelevel Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Experiencelevel Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteExperiencelevel(id):
        instances=Experiencelevel.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Experiencelevel Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Experiencelevel Details not found'}, status=status.HTTP_404_NOT_FOUND)

class GenderServices:
    def getAll():
        instances=Gender.objects.all()
        serialize=GenderSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getGender(id):
        instances=Gender.objects.filter(id=id).first()
        if instances:
            serializer=GenderSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Gender Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Gender(request,method,id=None):
        instances=Gender.objects.filter(id=id).first()
        serialize_data=GenderSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Gender Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=GenderSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Gender Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Gender Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteGender(id):
        instances=Gender.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Gender Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Gender Details not found'}, status=status.HTTP_404_NOT_FOUND)

class JobrequisitionServices:
    def getAll():
        instances=Jobrequisition.objects.all()
        serialize=JobrequisitionSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getJobrequisition(id):
        instances=Jobrequisition.objects.filter(id=id).first()
        if instances:
            serializer=JobrequisitionSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Jobrequisition Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Jobrequisition(request,method,id=None):
        instances=Jobrequisition.objects.filter(id=id).first()
        serialize_data=JobrequisitionSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Jobrequisition Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=JobrequisitionSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Jobrequisition Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Jobrequisition Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteJobrequisition(id):
        instances=Jobrequisition.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Jobrequisition Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Jobrequisition Details not found'}, status=status.HTTP_404_NOT_FOUND)

class MaritalstatusServices:
    def getAll():
        instances=Maritalstatus.objects.all()
        serialize=MaritalstatusSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getMaritalstatus(id):
        instances=Maritalstatus.objects.filter(id=id).first()
        if instances:
            serializer=MaritalstatusSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Maritalstatus Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Maritalstatus(request,method,id=None):
        instances=Maritalstatus.objects.filter(id=id).first()
        serialize_data=MaritalstatusSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Maritalstatus Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=MaritalstatusSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Maritalstatus Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Maritalstatus Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteMaritalstatus(id):
        instances=Maritalstatus.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Maritalstatus Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Maritalstatus Details not found'}, status=status.HTTP_404_NOT_FOUND)

class PersonaServices:
    def getAll():
        instances=Persona.objects.all()
        serialize=PersonaSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getPersona(id):
        instances=Persona.objects.filter(id=id).first()
        if instances:
            serializer=PersonaSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Persona Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Persona(request,method,id=None):
        instances=Persona.objects.filter(id=id).first()
        serialize_data=PersonaSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Persona Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=PersonaSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Persona Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Persona Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deletePersona(id):
        instances=Persona.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Persona Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Persona Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
class ReasonforchangeServices:
    def getAll():
        instances=Reasonforchange.objects.all()
        serialize=ReasonforchangeSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getReasonforchange(id):
        instances=Reasonforchange.objects.filter(id=id).first()
        if instances:
            serializer=ReasonforchangeSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Reasonforchange Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Reasonforchange(request,method,id=None):
        instances=Reasonforchange.objects.filter(id=id).first()
        serialize_data=ReasonforchangeSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Reasonforchange Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=ReasonforchangeSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Reasonforchange Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Reasonforchange Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteReasonforchange(id):
        instances=Reasonforchange.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Reasonforchange Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Reasonforchange Details not found'}, status=status.HTTP_404_NOT_FOUND)

class ScreeningmodeServices:
    def getAll():
        instances=Screeningmode.objects.all()
        serialize=ScreeningmodeSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getScreeningmode(id):
        instances=Screeningmode.objects.filter(id=id).first()
        if instances:
            serializer=ScreeningmodeSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Screeningmode Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Screeningmode(request,method,id=None):
        instances=Screeningmode.objects.filter(id=id).first()
        serialize_data=ScreeningmodeSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Screeningmode Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=ScreeningmodeSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Screeningmode Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Screeningmode Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteScreeningmode(id):
        instances=Screeningmode.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Screeningmode Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Screeningmode Details not found'}, status=status.HTTP_404_NOT_FOUND)

class SourceServices:
    def getAll():
        instances=Source.objects.all()
        serialize=SourceSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getSource(id):
        instances=Source.objects.filter(id=id).first()
        if instances:
            serializer=SourceSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Source Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Source(request,method,id=None):
        instances=Source.objects.filter(id=id).first()
        serialize_data=SourceSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Source Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=SourceSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Source Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Source Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteSource(id):
        instances=Source.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Source Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Source Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
class SourcetypeServices:
    def getAll():
        instances=Sourcetype.objects.all()
        serialize=SourcetypeSerializer(instances,many=True)
        return Response({'data':serialize.data},status=status.HTTP_200_OK)
    
    def getSourcetype(id):
        instances=Sourcetype.objects.filter(id=id).first()
        if instances:
            serializer=SourcetypeSerializer(instances)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Sourcetype Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def create_or_Update_Sourcetype(request,method,id=None):
        instances=Sourcetype.objects.filter(id=id).first()
        serialize_data=SourcetypeSerializer(data=request.data)
        if method == 'POST':
            if serialize_data.is_valid():
                serialize_data.save()
                return Response({'Message': 'Sourcetype Added Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serialize_data.errors}, status=status.HTTP_200_OK)
        elif method == 'PUT' and instances:
            serializer=SourcetypeSerializer(instances,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Sourcetype Updated Successfully'}, status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors}, status=status.HTTP_200_OK)
        return Response({'Message': 'Sourcetype Details not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def deleteSourcetype(id):
        instances=Sourcetype.objects.filter(id=id).first()
        if instances:
            instances.delete()
            return Response({'Message': 'Sourcetype Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'Message': 'Sourcetype Details not found'}, status=status.HTTP_404_NOT_FOUND)




