from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm

class Noteform(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title","body"]
        
class Date(forms.DateInput):
    input_type = 'date'        
        
class Homeworkform(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {"due":Date}
        fields = ["subject","title","body","due","done"] 
        
class dashbordform(forms.Form):
    text = forms.CharField(max_length=20, label="Enter your search: ")  
    
    
class Todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finish']    
        
class conversionform(forms.Form):
    Choice = [
        ('lenght','Lenght'),
        ('mass','Mass'),
        ('tempreture','Tempreture')
    ]  
    measurement = forms.ChoiceField(choices=Choice,widget=forms.RadioSelect) 
    
class Lenghtform(forms.Form):
    Choice = [
        ('meter','Meter'),
        ('centimeter','Centimeter')
    ]
    input = forms.CharField(required=False, label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter number'}
    ))   
    measure1 = forms.CharField(label='', widget=forms.Select(choices=Choice))   
    measure2 = forms.CharField(label='', widget=forms.Select(choices=Choice))   
    
    
    
class Massform(forms.Form):
    Choice = [
        ('gram','Gram'),
        ('kilogram','Kilogram')
    ]
    input = forms.CharField(required=False, label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter number'}
    ))   
    measure1 = forms.CharField(label='', widget=forms.Select(choices=Choice))   
    measure2 = forms.CharField(label='', widget=forms.Select(choices=Choice))    
    
    
class Tempretureform(forms.Form):
    Choice = [
        ('kelvin','Kelvin'),
        ('celcius','Celcius'),
        ('farentheight','Farentheight')
    ]
    input = forms.CharField(required=False, label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter number'}
    ))   
    measure1 = forms.CharField(label='', widget=forms.Select(choices=Choice))   
    measure2 = forms.CharField(label='', widget=forms.Select(choices=Choice))
    measure3 = forms.CharField(label='', widget=forms.Select(choices=Choice))        
                 
        
        
class Register(UserCreationForm):
    class Meta:
      model = User
      fields = ['username','email','password1','password2']