from django import forms
from .models import ProgressNote


class ProgressNoteForm(forms.ModelForm):
  class Meta:
    model = ProgressNote
    fields = ['note_type', 'content', 'is_visible_to_student']
