from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

## class for User Registration Form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_Name = forms.CharField()
    last_Name = forms.CharField()

    ## This Meta class will allow us to change the properties of parent form. 
    class Meta:
        model = User    ## Information will be saved into USER Model
        fields = ['email', 'username', 'first_Name', 'last_Name', 'password1', 'password2']  ## list of fields in order wise