from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Define a class for the auth class Form(forms.Form):
class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password', 'confirm_password']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
        }
    
class StaffAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Please check your credentials and try again'
    }    
    username = forms.CharField(error_messages= {'required': 'Please enter the username'})             
    password = forms.CharField(error_messages= {'required': 'Please enter the password'}) 
    