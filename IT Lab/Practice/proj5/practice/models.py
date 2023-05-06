from django.db import models
from django import forms
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_num = models.CharField(max_length=11)
    branch = models.CharField(max_length=100)
    cgpa = models.CharField(max_length=3)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = {}


