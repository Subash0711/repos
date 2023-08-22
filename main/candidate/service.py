from rest_framework import viewsets
from candidate.models import ( Candidatedirectory)
from candidate.serializers import (PersonalSerializer, EducationSerializer, WorkSerializer, ApplicationSerializer, LoginSerializer)
from rest_framework.response import Response
from rest_framework import status

class CoreServices:
    @classmethod
    def getAllDeatils(cls, id):
        queryset = Candidatedirectory.objects.filter(id=id).first()
        return queryset

    @classmethod
    def deleteprofile(cls, id):
        instance = cls.getAllDeatils(id)
        if instance:
            instance.delete()
            return Response({'Message': 'User Profile Deleted Successfully'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'Message': 'User Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        
class PersonalDetailsServices:

    @classmethod
    def get_personal_details(cls, id):
        instance = CoreServices.getAllDeatils(id=id)
        if instance:
            serializer = PersonalSerializer(instance)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'Personal Details not found'}, status=status.HTTP_404_NOT_FOUND)

    @classmethod
    def create_personal_details(cls, request):
        serializer = PersonalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'Personal Details Added Successfully)'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def update_personal_details(cls, request, id):
        instances = CoreServices.getAllDeatils(id)
        serializer = PersonalSerializer(instances, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'Personal Details updated Successfully)'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EducationDetailsServices:

    @classmethod
    def get_Education_details(cls, id):
        instance = CoreServices.getAllDeatils(id=id)
        if instance:
            serializer = EducationSerializer(instance)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'Message': 'Education Details not found'}, status=status.HTTP_404_NOT_FOUND)

    @classmethod
    def create_or_update_Education_details(cls, request, id,method):
        instance = CoreServices.getAllDeatils(id)
        if not request.data:
            return Response({'Message': 'Data Not Provided'}, status=status.HTTP_400_BAD_REQUEST)
        if instance:
            if method == 'POST':
                serializer = EducationSerializer(instance, data=request.data)
            else:
                serializer = EducationSerializer(instance, data=request.data,partial=True)
            if serializer.is_valid():
                if method == 'POST':
                    serializer.save()
                    return Response({'Message': 'Education Details Added Successfully'}, status=status.HTTP_201_CREATED)
                else:
                    serializer.save()
                    return Response({'Message': 'Education Details Updated Successfully'}, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message': 'Education Details not found'}, status=status.HTTP_404_NOT_FOUND)

class WorkDetailsServices:

    @classmethod
    def get_work_details(cls, id):
        instance = CoreServices.getAllDeatils(id=id)
        if instance:
            serializer = WorkSerializer(instance)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'Work Details not found'}, status=status.HTTP_404_NOT_FOUND)

    @classmethod
    def create_or_update_work_details(cls, request, id,method):
        instance = CoreServices.getAllDeatils(id)
        if not request.data:
            return Response({'Message': 'Data Not Provided'}, status=status.HTTP_400_BAD_REQUEST)
        if instance:
            if method == 'POST':
                serializer = WorkSerializer(instance, data=request.data)
            else:
                serializer = WorkSerializer(instance, data=request.data,partial=True)

            if serializer.is_valid() :
                if method == 'POST':
                    serializer.save()
                    return Response({'Message': 'Work Details Added Successfully'}, status=status.HTTP_201_CREATED)
                else:
                    serializer.save()
                    return Response({'Message': 'Work Details Updated Successfully'}, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message': 'Work Details not found'}, status=status.HTTP_404_NOT_FOUND)

class ApplicationDetailsServices:

    @classmethod
    def get_Application_details(cls, id):
        instance = CoreServices.getAllDeatils(id=id)
        if instance:
            serializer = ApplicationSerializer(instance)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'Application Details not found'}, status=status.HTTP_404_NOT_FOUND)

    @classmethod
    def create_or_update_Application_details(cls, request, id,method):
        instance = CoreServices.getAllDeatils(id)
        if not request.data:
            return Response({'Message': 'Data Not Provided'}, status=status.HTTP_400_BAD_REQUEST)
        if instance:
            if method == 'POST':
                serializer = WorkSerializer(instance, data=request.data)
            else:
                serializer = WorkSerializer(instance, data=request.data,partial=True)
            if serializer.is_valid():
                if method == 'POST':
                    serializer.save()
                    return Response({'Message': 'Application Details Added Successfully'}, status=status.HTTP_201_CREATED)
                else:
                    serializer.save()
                    return Response({'Message': 'Application Details Updated Successfully'}, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message': 'Work Details not found'}, status=status.HTTP_404_NOT_FOUND)

class CandidateLoginDetailsServices:

    @classmethod
    def get_login_details(cls, id):
        instance = CoreServices.getAllDeatils(id=id)
        if instance:
            serializer = LoginSerializer(instance)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'Login Details not found'}, status=status.HTTP_404_NOT_FOUND)

    @classmethod
    def create_or_update_login_details(cls, request, id,method):
        instance = CoreServices.getAllDeatils(id)
        if not request.data:
            return Response({'Message': 'Data Not Provided'}, status=status.HTTP_400_BAD_REQUEST)
        if instance:
            if method == 'POST':
                serializer = LoginSerializer(instance, data=request.data)
            else:
                serializer = LoginSerializer(instance, data=request.data,partial=True)

            if serializer.is_valid():
                if method == 'POST':
                    serializer.save()
                    return Response({'Message': 'Login Details Added Successfully'}, status=status.HTTP_201_CREATED)
                else:    
                    serializer.save()
                    return Response({'Message': 'Login Details Updated Successfully'}, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message': 'Login Details not found'}, status=status.HTTP_404_NOT_FOUND)
