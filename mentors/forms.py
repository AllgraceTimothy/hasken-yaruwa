from django import forms
from .models import Mentor

class MentorForm(forms.ModelForm):
  class Meta:
    model = Mentor
    fields = [
      'full_name',
      'email',
      'phone_no',
      'background',
      'motivation',
    ]