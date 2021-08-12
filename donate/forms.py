from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  DonorsInfo




class CreateUserForms(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        
        

    

class DonorForms(forms.ModelForm):
    class Meta:
        model = DonorsInfo
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'age' : forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': 'radio'}) ,
            'blood_group': forms.RadioSelect(attrs={'class': 'radio'}), 
            'weight' : forms.NumberInput(attrs={'class': 'form-control'}),
            'negative_tested_on' : forms.DateInput(attrs={'class': 'form-control'}),
            'city' : forms.TextInput(attrs={'class': 'form-control'}),
            'donate_center' : forms.Select(attrs={'class': 'form-select'}),
            }
        

