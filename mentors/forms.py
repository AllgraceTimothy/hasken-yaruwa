from django import forms
from .models import Mentors

class MentorForm(forms.ModelForm):
  class Meta:
    model = Mentors
    fields = [
      'full_name',
      'email',
      'phone',
      'background',
      'motivation',
    ]