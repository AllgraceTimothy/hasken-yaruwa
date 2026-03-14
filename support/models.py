from django.db import models
from students.models import Student

class Support(models.Model):
  source = models.CharField(max_length=200)
  description = models.TextField(blank=True)

  amount = models.DecimalField(
    max_digits=12,
    decimal_places=2
  )

  date_received = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.source} - {self.amount}"
  
class ResourceAllocation(models.Model):

    RESOURCE_TYPES = [
        ('scholarship', 'Scholarship'),
        ('laptop', 'Laptop'),
        ('books', 'Books'),
        ('transport', 'Transport Support'),
        ('internet', 'Internet Access'),
        ('training', 'Training Program'),
        ('other', 'Other Support'),
    ]

    resource_type = models.CharField(
        max_length=50,
        choices=RESOURCE_TYPES
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="support_received"
    )

    support_source = models.ForeignKey(
        Support,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    quantity = models.IntegerField(default=1)

    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    date_allocated = models.DateField(auto_now_add=True)

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_resource_type_display()} → {self.student.user.full_name}"
  
class ImpactMetric(models.Model):
  title = models.CharField(max_length=200)
  value = models.IntegerField()
  description = models.TextField(blank=True)
  order = models.IntegerField(default=0)

  def __str__(self):
    return self.title
