from django.db import models

APPLICATION_STATUSES = (
  ('submitted', 'Submitted'),
  ('approved', 'Approved'),
  ('rejected', 'Rejected'),
)
class StudentApplication(models.Model):
  full_name = models.CharField(max_length=200)
  email = models.EmailField(max_length=254, unique=True, blank=False, null=False)
  age = models.PositiveIntegerField()
  school_name = models.CharField(max_length=200)
  location = models.CharField(max_length=200)

  parent_name = models.CharField(max_length=200)
  parent_contact = models.CharField(max_length=50)

  main_challenge = models.CharField(max_length=200)
  personal_story = models.TextField(blank=True)

  status = models.CharField(
    max_length=20,
    choices=APPLICATION_STATUSES,
    default='submitted'
  )

  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Student: {self.full_name}"

class MentorApplication(models.Model):
  full_name = models.CharField(max_length=200)
  email = models.EmailField(max_length=254, unique=True, blank=False, null=False)
  phone_no = models.CharField(max_length=50)
  background = models.TextField()
  motivation = models.TextField()

  status = models.CharField(
    max_length=20,
    choices=APPLICATION_STATUSES,
    default='submitted'
  )
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Mentor: {self.full_name}"