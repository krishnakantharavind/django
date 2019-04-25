from __future__ import unicode_literals 
from django.db import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.us.models import USPostalCodeField, USStateField, USSocialSecurityNumberField, USZipCodeField
from localflavor.in_.forms import INAadhaarNumberField
from localflavor.in_.in_states import STATE_CHOICES
from django_countries import countries
import pytz
from django.forms import ModelForm
COUNTRY_CHOICES = tuple(countries)
TIMEZONE_CHOICES = tuple((choice, choice) for choice in pytz.common_timezones)
GENDER_CHOICES = (
				('',''),
				('male','Male'),
				('female', 'Female'),
			)
PROFICIENCY_CHOICES = (
				('',''),
				('good','Good'),
				('average', 'Average'),
				('excellent','Excellent'),
				('poor','Poor'),
			)
class Student(models.Model): 
    candidate_registration_no = models.SlugField()
    first_name = models.CharField(max_length=20) 
    middle_name= models.CharField(max_length=10)	
    last_name  = models.CharField(max_length=30) 	
    email      = models.EmailField(max_length=50)  
    age        = models.IntegerField()
    #image      = models.ImageField()	
    DOB        = models.DateField()
    gender    = models.CharField(max_length=10, choices=GENDER_CHOICES)
    state    =   models.CharField(max_length=20, choices=STATE_CHOICES)
    country  =   models.CharField(max_length=20, choices=COUNTRY_CHOICES)
    address_line_1 = models.TextField(max_length=50)
    address_line_2 = models.TextField(max_length=30)
    zipcode = USZipCodeField()
    phone_number = PhoneNumberField()
    #resume = models.FileField()
	



class Language(models.Model):
    language_name= models.CharField(max_length=20)
class Student_Language(models.Model):
    student_id = models.ForeignKey(Student, on_delete='CASCADE')
    read_language=models.ManyToManyField(Language, related_name='read_language')
    speak_language=models.ManyToManyField(Language, related_name='speak_language')
    write_language=models.ManyToManyField(Language, related_name='write_language')
    reading_proficiency=models.CharField(max_length=20,choices=PROFICIENCY_CHOICES)
    speaking_proficiency=models.CharField(max_length=20,choices=PROFICIENCY_CHOICES)
    writing_proficiency=models.CharField(max_length=20,choices=PROFICIENCY_CHOICES)
class Skill_Categories(models.Model):
    skill_category_code=models.SlugField()
    skill_category_name=models.CharField(max_length=20)
class Skill(models.Model):
    skill_code=models.SlugField()
    skill_name=models.CharField(max_length=20)
    skill_category_id=models.ForeignKey(Skill_Categories,on_delete='CASCADE')
class Student_Skill(models.Model):
    student_id = models.ForeignKey(Student, on_delete='CASCADE')
    skill_id = models.ManyToManyField(Skill)
    skill_proficiency=models.CharField(max_length=10, choices=PROFICIENCY_CHOICES)
    experience=models.SlugField()
class Student_Certificate(models.Model):
    student_id= models.ForeignKey(Student, on_delete='CASCADE')
    certificate_code=models.SlugField()
    certificate_description=models.TextField(max_length=100)
    institution_name=models.TextField(max_length=50)
    certificate_validity=models.DateField()
    certificate_duration=models.CharField(max_length=10)
class Student_Academics(models.Model):
    student_id=models.ForeignKey(Student, on_delete='CASCADE')
    register_number=models.BigIntegerField()
    graduated=models.BooleanField()
    graduated_on=models.DateField()
    major=models.CharField(max_length=20)
    university_name=models.TextField(max_length=50)
    CGPA=models.DecimalField(max_digits=4,decimal_places=2)
class Student_Employment_History(models.Model):
    student_id=models.ForeignKey(Student,on_delete='CASCADE')
    date_of_joining=models.DateField()
    date_of_relieving=models.DateField()
    company_name=models.TextField(max_length=50)
    designation=models.CharField(max_length=20)
    employment_status=models.BooleanField()
class Visa_Categories(models.Model):
    country_name=models.CharField(max_length=50,choices=COUNTRY_CHOICES)
    country_code=models.CharField(max_length=10)
class Student_Visa(models.Model):
    student_id=models.ForeignKey(Student,on_delete='CASCADE')
    visa_code=models.SlugField()
    visa_category_id=models.ManyToManyField(Visa_Categories)
    visa_validity=models.DateField()
    visa_status=models.BooleanField()
    issued_for=models.CharField(max_length=20,choices=COUNTRY_CHOICES)
class Student_Passport(models.Model): 
    student_id=models.ForeignKey(Student,on_delete='CASCADE')
    candidate_name_as_on_passport=models.CharField(max_length=50)
    passport_number=models.BigIntegerField()
    passport_validity=models.DateField()
    passport_status=models.BooleanField()
    passport_issued_at=models.TextField(max_length=50)

# Register your models here.