from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Student