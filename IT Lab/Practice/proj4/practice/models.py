from django.db import models
from django import forms


class Employee(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    email = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = {}
