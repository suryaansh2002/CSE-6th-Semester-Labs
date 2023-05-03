from django.db import models
from django import forms
# Create your models here.


class BookModel(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    borrowed = models.CharField(max_length=100, default='No')
    genres = ['thriller', 'horror', 'romance']
    genre = models.CharField(
        choices=[(x, x) for x in genres], default=genres[0], max_length=100)


class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        exclude = {'borrowed'}


class IssueModel(models.Model):
    student_name = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    issue_date = models.CharField(max_length=20)


class IssueForm(forms.ModelForm):
    class Meta:
        model = IssueModel
        exclude = {}
