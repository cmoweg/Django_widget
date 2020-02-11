# core/forms.py

from django import forms
from .models import University, Student
from .widgets import CounterTextInput, AutoCompleteWidget, starWidget


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name']
        widgets = {
            'name': CounterTextInput,
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'university': AutoCompleteWidget,
            'grade': starWidget,
        }