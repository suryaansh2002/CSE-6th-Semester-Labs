from django.shortcuts import render
from .models import userModel, userForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(req):
    if req.method == "POST":
        form = userForm(req.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect("/")
    context = {}
    context["form"] = userForm()
    context["users"] = userModel.objects.all()
    return render(req, "index.html", context)
