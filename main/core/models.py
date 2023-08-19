from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'city'


class Educationlevel(models.Model):
    education_level = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'educationlevel'

class Educationqualification(models.Model):
    education_qualification = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'educationqualification'

class Educationspecialization(models.Model):
    education_specialization = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'educationspecialization'

class Employeedirectory(models.Model):
    referred_by = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'employeedirectory'

class Eventdetails(models.Model):
    event = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'eventdetails'

class Experiencelevel(models.Model):
    experience_level = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'experiencelevel'

class Gender(models.Model):
    gender = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'gender'

class Jobrequisition(models.Model):
    job_position = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'jobrequisition'

class Maritalstatus(models.Model):
    marital_status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'maritalstatus'

class Persona(models.Model):
    persona = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'persona'

class Reasonforchange(models.Model):
    reason_for_change = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'reasonforchange'

class Screeningmode(models.Model):
    screening_mode = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'screeningmode'

class Source(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'source'

class Sourcetype(models.Model):
    type_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sourcetype'