from django import forms
from .models import Candidate

class Candidateform(forms.ModelForm):
    class Meta:
        model =  Candidate
        fields = ('name' ,'email' , 'enrolno' ,'branch' ,'bio','image')
        
        labels = {
            'name':'',
            'email':'',
            'enrolno' : '',
            'branch':'Branch',
            'bio' : '',
            'image':'',

        }

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Name'} ,),
            'email':forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'Email'}),
            'branch': forms.Select(attrs={ 'class':'form-select', 'placeholder' : 'Branch'}),
            'enrolno' : forms.NumberInput(attrs={'class':'form-control', 'placeholder' : 'Enrollment Number'}),
            'bio' : forms.Textarea(attrs={'class' : 'form-control' , 'placeholder' : 'Something about Yourself'}),
        }