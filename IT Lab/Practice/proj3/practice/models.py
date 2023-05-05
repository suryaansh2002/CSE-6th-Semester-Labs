from django.db import models
from django import forms

# Create your models here.


class userModel(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    address = models.CharField(max_length=500)
    dob = models.CharField(max_length=100)


class userForm(forms.ModelForm):
    class Meta:
        model = userModel
        exclude = {}
