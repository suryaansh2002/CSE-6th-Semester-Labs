from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BookForm, BookModel, IssueModel, IssueForm


def index(req):
    return render(req, 'index.html', {})


def bookForm(req):
    if(req.method == 'POST'):
        form = BookForm(req.POST)
        if(form.is_valid()):
            obj = form.save(commit=False)
            obj.save()
    context = {}
    context['form'] = BookForm()
    return render(req, 'bookForm.html', context)


def books(req):
    context = {}
    context['books'] = BookModel.objects.all()
    return render(req, 'books.html', context)


def issueForm(req):
    if(req.method == 'POST'):
        form = IssueForm(req.POST)
        if(form.is_valid()):
            obj = form.save(commit=False)
            obj.save()
    context = {}
    context['form'] = IssueForm()
    return render(req, 'issueForm.html', context)


def issues(req):
    context = {}
    context['issues'] = IssueModel.objects.all()
    return render(req, 'issues.html', context)
