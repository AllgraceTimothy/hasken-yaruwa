from django.db import models
from accounts.models import User
from applications.models import MentorApplication


class Mentor(models.Model):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name='mentor_profile'
  )

  application = models.OneToOneField(
    MentorApplication,
    on_delete=models.CASCADE
  )

  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Mentor: {self.user.full_name}"
