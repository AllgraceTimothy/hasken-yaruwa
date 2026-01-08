from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
  class Meta:
    model = Application
    fields = [
      'full_name',
      'age',
      'school_name',
      'location',
      'parent_name',
      'parent_contact',
      'main_challenge',
      'personal_story',
    ]