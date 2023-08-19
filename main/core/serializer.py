from rest_framework import serializers
from core.models import (
    City, Educationlevel, Educationqualification,
    Educationspecialization, Employeedirectory, Eventdetails,
    Experiencelevel, Gender, Jobrequisition, Maritalstatus,
    Persona, Reasonforchange, Screeningmode, Source, Sourcetype
)

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class EducationlevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educationlevel
        fields = '__all__'

class EducationqualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educationqualification
        fields = '__all__'

class EducationspecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educationspecialization
        fields = '__all__'

class EmployeedirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeedirectory
        fields = '__all__'

class EventdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventdetails
        fields = '__all__'

class ExperiencelevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencelevel
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class JobrequisitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobrequisition
        fields = '__all__'

class MaritalstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maritalstatus
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class ReasonforchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reasonforchange
        fields = '__all__'

class ScreeningmodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screeningmode
        fields = '__all__'

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class SourcetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sourcetype
        fields = '__all__'
