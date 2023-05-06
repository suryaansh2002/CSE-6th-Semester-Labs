from django.shortcuts import render
from .models import Employee, EmployeeForm
from django.http import HttpResponseRedirect


def index(req):
    if(req.method == 'POST'):
        form = EmployeeForm(req.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
        return HttpResponseRedirect('/')

    context = {}
    context['form'] = EmployeeForm
    context['employees'] = Employee.objects.all()
    return render(req, 'index.html', context)
