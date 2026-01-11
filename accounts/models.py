from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models
import random
import string

class UserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError("Email is required")

    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('role', 'admin')
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
  ROLE_CHOICES = (
    ('student', 'Student'),
    ('mentor', 'Mentor'),
    ('admin', 'Admin'),
  )

  email = models.EmailField(unique=True)
  full_name = models.CharField(max_length=200)

  role = models.CharField(
    max_length=20,
    choices=ROLE_CHOICES
  )

  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  date_joined = models.DateTimeField(auto_now_add=True)

  objects = UserManager()
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['full_name', 'role']

  def __str__(self):
    return f"{self.full_name} ({self.role})"

  
# Random Password Generator
def make_random_password(length=12):
  characters = string.ascii_letters + string.digits  # a-zA-Z0-9
  return ''.join(random.choice(characters) for _ in range(length))