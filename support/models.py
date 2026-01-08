from django.db import models

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
