from django import forms
from django.contrib.auth.models import User as UR
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = '__all__'
        exclude = ['id', 'is_present', 'updated']
        labels = {'name':'Enter Name', 'enrollmentno': 'Enter enrollment No.','phone':'Enter Phone No.',
                  'email':'Enter Email','image':'Upload student Profile pic'
                  }
        
class UserLogin(forms.ModelForm):
    class Meta:
        model = UR
        fields = ['username', 'password']
        labels = {'Username':'Enter Username', 'password':'Enter Password'}