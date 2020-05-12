from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime


class Activity_Form(forms.Form):

    event_attrs = {
        'type': 'text',
        'class': 'validate',
        'placeholder': 'Event Name'
    }

    date_attrs = {
        'type': 'date',
        'class': 'datepicker',
        'placeholder': 'Date of Event'
    }

    time_attrs = {
        'type': 'time',
        'class': 'timepicker',
        'placeholder': 'Time of Event'
    }

    category_attrs = {
        'type': 'text',
        'class': 'validate',
        'placeholder': 'Category'
    }

    location_attrs = {
        'type': 'text',
        'class': 'validate',
        'placeholder': 'Location of Event'
    }

    


    eventName = forms.CharField(label = '', required=True, widget=forms.TextInput(attrs=event_attrs)) # name of the activity
    
    date = forms.DateField(label='', required=True,
            widget=forms.DateInput(attrs=date_attrs))

    time = forms.TimeField(label='Time', required=True, widget=forms.TimeInput(attrs=time_attrs))
    category = forms.CharField(label = '', required=True, widget=forms.TextInput(attrs=category_attrs))
    location = forms.CharField(label = '', required=True, widget=forms.TextInput(attrs=location_attrs))

class Registration_Form(forms.Form):

    firstname_attrs = {
        'type': 'text',
        'class': 'validate',
        'placeholder': 'First Name',
        'name' : 'firstname'
    }

    lastname_attrs = {
        'type': 'text',
        'class': 'validate',
        'placeholder': 'Last Name',
        'name' : 'lastname'
    }

    email_attrs = {
        'type': 'text',
        'class': 'validate',
        'placeholder': 'Email',
        'id' : 'email',
        'name' : 'emailname'
    }

    password_attrs = {
        # 'type': 'text',
        'class': 'validate',
        'placeholder': 'Password',
        'name' : 'password'
    }



    firstname = forms.CharField(label = 'First Name', required=True, 
            widget=forms.TextInput(attrs=firstname_attrs)) # name of the activity
    
    lastname = forms.CharField(label='Last Name', required=True,
            widget=forms.TextInput(attrs=lastname_attrs) )

    email = forms.CharField(label='Email', required=True,
            widget=forms.TextInput(attrs=email_attrs))

    password = forms.CharField(label='Password', required=True, 
            widget=forms.PasswordInput(attrs=password_attrs))

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        