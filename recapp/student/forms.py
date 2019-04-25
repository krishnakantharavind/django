from django.shortcuts import render
from django.forms import ModelForm
from student.models import Student
# Create your views here.
class studentform(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'