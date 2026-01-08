from django.db import models

class Application(models.Model):
  STATUSES = (
      ('submitted', 'Submitted'),
      ('approved', 'Approved'),
      ('rejected', 'Rejected'),
  )

  full_name = models.CharField(max_length=200)
  age = models.PositiveIntegerField()
  school_name = models.CharField(max_length=200)
  location = models.CharField(max_length=200)

  parent_name = models.CharField(max_length=200)
  parent_contact = models.CharField(max_length=50)

  main_challenge = models.CharField(max_length=200)
  personal_story = models.TextField(blank=True)

  status = models.CharField(
    max_length=20,
    choices=STATUSES,
    default='submitted'
  )

  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.full_name
