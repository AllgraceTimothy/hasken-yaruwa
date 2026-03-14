from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
  CATEGORY_CHOICES = [
    ('education', 'Education Access'),
    ('mentorship', 'Mentorship'),
    ('student_voice', 'Student Voices'),
    ('updates', 'Program Updates'),
    ('community', 'Community Impact'),
    ('research', 'Research & Insights'),
  ]

  title = models.CharField(max_length=250)
  slug = models.SlugField(unique=True, blank=True)

  category = models.CharField(
    max_length=50,
    choices=CATEGORY_CHOICES
  )

  content = models.TextField()

  featured_image = models.ImageField(
    upload_to='blog_images/',
    blank=True,
    null=True
  )

  published = models.BooleanField(default=False)

  created_at = models.DateTimeField(auto_now_add=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)

    super().save(*args, **kwargs)

  def __str__(self):
    return self.title
  
class SuccessStory(models.Model):
  student_name = models.CharField(max_length=200)
  title = models.CharField(max_length=250)
  story = models.TextField()
  photo = models.ImageField(
    upload_to='success_stories/',
    blank=True,
    null=True
  )
  graduation_year = models.IntegerField(
    blank=True,
    null=True
  )
  featured = models.BooleanField(default=False)
  published = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title