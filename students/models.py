from django.db import models
from applications.models import Application

class Student(models.Model):
  application = models.OneToOneField(
    Application,
    on_delete=models.CASCADE
  )

  enrolement_date = models.DateTimeField(auto_now_add=True)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.application.full_name
  
class StudentSupportNote(models.Model):
  student = models.ForeignKey(
    'Student',
    on_delete=models.CASCADE
  )
  note = models.TextField()
  date = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.student.application.full_name