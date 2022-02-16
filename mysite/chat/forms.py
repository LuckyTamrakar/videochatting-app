from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField




class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone_no = forms.CharField(max_length = 20)
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	enroll_no = forms.CharField(max_length = 20)
	captcha = CaptchaField()
	class Meta:
		model = User
		fields = ['username', 'email', 'phone_no', 'password1', 'password2','enroll_no']


class createuserform(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','password'] 



