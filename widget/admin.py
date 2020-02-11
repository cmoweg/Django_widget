from django.contrib import admin
from .models import University, Student
from .forms import UniversityForm, StudentForm


@admin.register(University)
class CountryAdmin(admin.ModelAdmin):
    form = UniversityForm


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
