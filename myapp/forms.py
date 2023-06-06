from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email','roll_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'roll_id': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            
            
        }