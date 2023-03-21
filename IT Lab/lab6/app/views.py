from django.shortcuts import render
from .forms import InputForm, FirstForm, RegisterForm, DeviceForm
from django.http import HttpResponse, HttpResponseRedirect
import urllib.parse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
 
def home_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            params = {
                "manufacturers" : form.cleaned_data["manufacturers"],
                "model_name" : form.cleaned_data["model_name"],
            }
            q_string = urllib.parse.urlencode(params)
            redirect_url = "/app/success?{}".format(q_string)
            return HttpResponseRedirect(redirect_url)
    context ={}
    context['form']= InputForm()
    return render(request, "home1.html", context)


def success_view(request):
    manufacturers=request.GET['manufacturers']
    model_name=request.GET['model_name']
    context={'manufacturer': manufacturers, 'model_name':model_name}
    return render(request, "success1.html",context)

def first_form(request):
    if request.method == 'POST':
        form = FirstForm(request.POST)
        if form.is_valid():
            params = {
                "name" : form.cleaned_data["name"],
                "roll_no" : form.cleaned_data["roll_no"],
                "subject":form.cleaned_data["subject"]
            }
            q_string = urllib.parse.urlencode(params)
            redirect_url = "/app/second?{}".format(q_string)
            return HttpResponseRedirect(redirect_url)
    context ={}
    context['form']= FirstForm()
    return render(request, "first2.html", context)

def second_form(request):
    name=request.GET['name']
    roll_no=request.GET['roll_no']
    subject=request.GET['subject']
    context={'name':name, 'roll_no':roll_no, 'subject':subject}
    return render(request, "second2.html", context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            params ={
                "username" : form.cleaned_data["username"],
                "email" : form.cleaned_data["email_id"],
                "contact" : form.cleaned_data["contact_no"],
            }
            q_string = urllib.parse.urlencode(params)
            redirect_url = "/app/success3?{}".format(q_string)
            return HttpResponseRedirect(redirect_url)
    context ={}
    context['form']= RegisterForm()
    return render(request, "register3.html", context)

def success3_view(request):
    u=request.GET['username']
    e=request.GET['email']
    c=request.GET['contact']
    context={'username':u, 'email': e, 'contact':c}
    return render(request, "success3.html",context)


def device_view(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            params = {
                "brand" : form.cleaned_data["brand"],
                "quantity" : form.cleaned_data["quantity"],
                "device" : form.cleaned_data["device"],
            }
            q_string = urllib.parse.urlencode(params)
            redirect_url = "/app/bill4?{}".format(q_string)
            return HttpResponseRedirect(redirect_url)
    context ={}
    context['form']= DeviceForm()
    return render(request, "device4.html", context)

def bill4_view(request):
    b=request.GET['brand']
    q=int(request.GET['quantity'])
    d=request.GET['device'].split(',')
    d1=''
    d2=''
    if(len(d)==2):
        d1=d[0][2:-1]
        d2=d[1][2:-2]
    l=[d1,d2]
    p=0
    price={'HP':[100,500], 'Nokia':[100,500], 'Samsung':[100,500],'Motorolla':[100,500],'Apple':[100,500]}
    
    if('Mobile' in l):
        p+=price[b][0]
    if('Laptop' in l):
        p+=price[b][1]
    p*=q
    context={'brand':b, 'quantity': q, 'd1':d1, 'd2':d2, 'price': p}
    return render(request, "bill4.html",context)

