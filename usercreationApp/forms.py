from django import forms  
from .models import usercreate  
from django.contrib.auth.models import User  
  
class SignupForm(forms.ModelForm):  
    class Meta:  
        model = usercreate  
        exclude =('active',)