from django.db import models

class Mentors(models.Model):
  full_name = models.CharField(max_length=200)
  email = models.EmailField()
  phone = models.CharField(max_length=50)
  background = models.TextField()
  motivation = models.TextField()
  approved = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.full_name