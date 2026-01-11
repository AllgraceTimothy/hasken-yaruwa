from django.db import models
from accounts.models import User
from students.models import Student
from mentors.models import Mentor


class ProgressNote(models.Model):
  NOTE_TITLES = [
    ('weekly_checkin', 'Weekly Check-in'),
    ('academic', 'Academic Progress'),
    ('financial', 'Financial Aid Update'),
    ('personal', 'Personal Development'),
    ('attendance', 'Attendance & Engagement'),
    ('challenge', 'Challenges / Concerns'),
    ('goal', 'Goal Setting'),
    ('milestone', 'Milestone Achieved'),
    ('general', 'General Update'),
    ('admin', 'Admin Review'),
  ]

  student = models.ForeignKey(
    Student,
    on_delete=models.CASCADE,
    related_name='notes'
  )

  mentor = models.ForeignKey(
    Mentor,
    on_delete=models.CASCADE,
    related_name='notes'
  )

  author = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='written_notes'
  )

  note_type = models.CharField(
    max_length=30,
    choices=NOTE_TITLES
  )

  title = models.CharField(max_length=255)
  content = models.TextField()

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  is_visible_to_student = models.BooleanField(default=True)

  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.get_note_type_display()} - {self.student.user.full_name}"
