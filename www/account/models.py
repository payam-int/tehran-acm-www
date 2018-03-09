from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Field(models.Model):
    title = models.CharField(max_length=255)

class UserProfile(models.Model):
    student_id = models.IntegerField(max_length=9)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
