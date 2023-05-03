from django.shortcuts import render
from .models import CRModel, CRForm, IncForm
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    if(request.method == 'POST'):
        form = CRForm(request.POST)
        if(form.is_valid()):
            obj = form.save(commit=False)
            obj.save()

    context = {}
    context['form'] = CRForm
    context['form2'] = IncForm
    context['users'] = CRModel.objects.all()
    return render(request, 'index.html', context)


def inc(request):
    if(request.method == 'POST'):
        form = IncForm(request.POST)
        print("Here", form)
        if(form.is_valid()):
            print("Here 2")
            name = form.cleaned_data['name']
            print("Name" + name)
            # obj, created = CRModel.objects.update_or_create(
            #     pk=name,
            #     defaults={
            #         'count': 1
            #     }
            # )
            obj = CRModel.objects.get(pk=name)
            obj.count = obj.count+1
            obj.save()
            print(obj)
    return HttpResponseRedirect('/')


# Create your views here.
