from django import forms
from django.contrib.auth.models import User as UR
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = '__all__'
        exclude = ['id', 'is_present', 'updated']
        # labels = {'name':'Enter Name', 'enrollmentno': 'Enter enrollment No.','phone':'Enter Phone No.',
        #           'email':'Enter Email','image':'Upload student Profile pic'
        #           }
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        # self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['enrollmentno'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['course'].widget.attrs['class'] = 'form-control'
        # self.fields['profession'].widget.attrs['class'] = 'form-control'
        # self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        # self.fields['shift'].widget.attrs['class'] = 'form-control'
class UserLogin(forms.ModelForm):
    class Meta:
        model = UR
        fields = ['username', 'password']
        labels = {'Username':'Enter Username', 'password':'Enter Password'}