from django.db import models


# Create your models here.
class Messages(models.Model):
    user = models.CharField()
    message = models.TextField()
