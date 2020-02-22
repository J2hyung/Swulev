from django.contrib import admin
from .models import Lecture

# Register your models here.
@admin.register(Lecture)
class Lecture(admin.ModelAdmin):
    list_display = ['lectureid', 'lecturename', 'professor', 'semester']
