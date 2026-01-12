from django.db import models
from accounts.models import User
from applications.models import StudentApplication
from mentors.models import Mentor

class Student(models.Model):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name='student_profile'
  )

  application = models.OneToOneField(
    StudentApplication,
    on_delete=models.CASCADE
  )

  mentor = models.ForeignKey(
    Mentor,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='students',
  )

  enrollment_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Student: {self.user.full_name}"
