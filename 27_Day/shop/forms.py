from django import forms
from .models import *


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['stu_name','email','password']

        

class TeacherRegistrationForm(StudentRegistrationForm):
    class Meta(StudentRegistrationForm.Meta):
        model = User
        fields = ['teacher_name','email','password']