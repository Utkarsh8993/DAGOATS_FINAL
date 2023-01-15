from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget , AdminTimeWidget


class VenueForm(forms.ModelForm):
    class Meta:
        model =  Venue
        fields = ('name' ,'address')
        
        labels = {
            'name':'',
            'address':'',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Name'} ,),
            'address' : forms.Textarea(attrs={'class' : 'form-control' , 'placeholder' : 'Address'} ,),
           
        }



class EventForm(forms.ModelForm):
    yop = forms.SelectMultiple()
    
    class Meta:
        model =  Event
        fields = ('name' , 'venue' , 'date' , 'time' , 'duration' , 'yop' , 'description' , 'mobile' , 'email')
        
        labels = {
            'name':'',
            'venue':'Venue',
            'date' : 'Date of Event',
            'time' : 'Time of Commencement',
            'duration' : '',
            'yop':'Years to be invited',
            'branch':'Branch',
            'description' : '',
            'mobile':'',
            'email':'',

        }

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Name'} ,),
            'venue' : forms.Select(attrs={'class' : 'form-control' } ,),
            'date' : forms.SelectDateWidget(attrs={'class' : 'form-control' }),
            'time' : AdminTimeWidget(attrs={'class' : 'form-control'}),
            'yop': forms.Select(attrs={ 'class':'form-select', }),
            'branch': forms.Select(attrs={ 'class':'form-select', }),
            'duration' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Duration'}),
            'mobile' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Mobile Number'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'Email'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control' , 'placeholder' : 'Details of Event'}),
        }