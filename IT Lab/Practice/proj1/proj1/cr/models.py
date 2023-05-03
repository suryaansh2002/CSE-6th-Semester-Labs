from django.db import models
from django import forms

# Create your models here.


class CRModel(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    count = models.IntegerField(default=0)


class CRForm(forms.ModelForm):
    class Meta:
        model = CRModel
        exclude = {'count'}

class IncForm(forms.Form):
    name = forms.CharField(max_length=20)
