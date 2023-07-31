from django import forms
from crudapp.models import Students


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['firstname', 'lastname', 'email']
