from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Caption(models.Model):
    img_id = models.CharField(max_length=256, unique=True)
    worker = models.CharField(max_length=64)
    caption = models.CharField(max_length=2048)