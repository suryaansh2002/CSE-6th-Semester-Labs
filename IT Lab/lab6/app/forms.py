# import the standard Django Forms
# from built-in library
from django import forms
   
# creating a form 
class InputForm(forms.Form):
    l=['Tata', 'Maruti', 'BMW', 'Audi']
    manufacturers =forms.ChoiceField(choices=[(x,x) for x in l])
    model_name = forms.CharField(max_length = 200)

class FirstForm(forms.Form):
    sub=['Physics','Chemsitry','Math', 'Bio']
    
    name = forms.CharField(max_length = 200)
    roll_no = forms.CharField(max_length = 200)
    subject =forms.ChoiceField(choices=[(x,x) for x in sub])
    
class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 200)
    password = forms.CharField(max_length = 200, widget=forms.PasswordInput())
    email_id = forms.CharField(max_length = 200)
    contact_no = forms.CharField(max_length = 200)
    
class DeviceForm(forms.Form):
    CHOICES = [
        'HP', 'Nokia', 'Samsung','Motorolla','Apple',
    ]
    brand = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[(x,x) for x in CHOICES], 
    )
    devices=[
        ('Mobile','Mobile'),
        ('Laptop', 'Laptop')
    ]
    quantity = forms.IntegerField()
    device = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=devices,
    )
