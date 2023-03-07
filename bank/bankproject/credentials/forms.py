from .models import User_details
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User_details
        fields = ['name','dob','age','gender','phno','mailid','addres','district','branch','account_type','materials']