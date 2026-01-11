from django import forms
from .models import StudentApplication, MentorApplication

class StudentApplicationForm(forms.ModelForm):
  class Meta:
    model = StudentApplication
    fields = [
      'full_name',
      'email',
      'age',
      'school_name',
      'location',
      'parent_name',
      'parent_contact',
      'main_challenge',
      'personal_story',
    ]

class MentorApplicationForm(forms.ModelForm):
  class Meta:
    model = MentorApplication
    fields = [
      'full_name',
      'email',
      'phone_no',
      'background',
      'motivation',
    ]