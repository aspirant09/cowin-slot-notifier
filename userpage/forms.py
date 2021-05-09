from django import forms
from .models import UserDetails

class UserForm(forms.ModelForm):
    username=forms.CharField(max_length=20)
    email=forms.EmailField()
    pinCode=forms.CharField(max_length=6,required=False)
    #fields = ['username','email'] 
    class  Meta:
        model=UserDetails
        fields = ['username','email',"pinCode"]