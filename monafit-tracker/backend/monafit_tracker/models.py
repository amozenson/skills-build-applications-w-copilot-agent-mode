from django.db import models

class FitnessEntry(models.Model):
    student_name = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.student_name} - {self.activity} on {self.date}"
