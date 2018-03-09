from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class StudentField(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    student_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    field = models.ForeignKey(StudentField, on_delete=models.CASCADE)
