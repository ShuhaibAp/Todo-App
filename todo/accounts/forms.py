from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "login-input", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "login-input", "placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"class": "login-input", "placeholder": "Email"}),
            "username": forms.TextInput(attrs={"class": "login-input", "placeholder": "Username"}),
        }
    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'login-input', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'login-input', 'placeholder': 'Confirm Password'})

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"login-input","placeholder":"Username"}))
    password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"login-input","placeholder":"Password"}))