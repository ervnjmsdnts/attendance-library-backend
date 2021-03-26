from django.db import models

# Create your models here.
class Section(models.Model):
    level = models.CharField(max_length=20)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class StudentAttendance(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    attendance_date = models.DateTimeField(auto_now_add=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
