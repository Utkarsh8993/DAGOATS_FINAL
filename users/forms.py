from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' ,'placeholder':'Email'}) , label='')
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Name'}) , label='')
    enrolno = forms.CharField(max_length=8 ,widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Enrollment Number'}) , label='')
    
    
    class Meta:
        model = User
        fields = ('email' , 'name' , 'enrolno', 'branch' ,'year', 'password1' , 'password2')

        def save(self , commit = True):
            user = super(RegisterForm , self).save(commit=False)
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user

    def __init__(self, *args , **kwargs):
        super(RegisterForm,self).__init__(*args , **kwargs)
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['branch'].widget.attrs['class'] = 'form-control'
        self.fields['branch'].label = 'Branch'
        self.fields['year'].widget.attrs['class'] = 'form-control'
        self.fields['year'].label = 'Year'