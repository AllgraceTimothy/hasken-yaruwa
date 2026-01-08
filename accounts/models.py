from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  USER_TYPES = (
    ('student', 'Student'),
    ('parent', 'Parent'),
    ('mentor', 'Mentor'),
    ('admin', 'Admin'),
  )
  role = models.CharField(max_length=20, choices=USER_TYPES)
