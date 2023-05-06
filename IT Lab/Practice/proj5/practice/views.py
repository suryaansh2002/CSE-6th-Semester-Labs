from django.shortcuts import render
from .models import Student, StudentForm
# Create your views here.
from django.http import HttpResponseRedirect


def index(req):
    if(req.method == 'POST'):
        form = StudentForm(req.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/')
    context = {}
    context['students'] = Student.objects.all()
    context['form'] = StudentForm()
    return render(req, 'index.html', context)
