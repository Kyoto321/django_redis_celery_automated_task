from django.forms import ModelForm
from django import forms
from . models import *

class MessageCreationForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'post a message', 'class':'p-4 text-black', 'max-length':'2000'}),
            
        }