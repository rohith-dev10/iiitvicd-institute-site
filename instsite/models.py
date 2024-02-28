from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    date=models.DateField(default=timezone.now)
    img_path=models.CharField(max_length=200)
    head=models.CharField(max_length=200)
    detail=models.TextField()

class Announcements(models.Model):
    date=models.DateField(default=timezone.now)
    head=models.CharField(max_length=200)
    detail=models.TextField()

class Hashes(models.Model):
    hash=models.CharField(max_length=100)

class Events(models.Model):
    time=models.CharField(max_length=16)
    date=models.DateField(default=timezone.now)
    img_path=models.CharField(max_length=200)
    head=models.CharField(max_length=200)
    detail=models.TextField()