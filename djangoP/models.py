from django.db import models


# Create your models here.
class Messages:
    user = models.CharField()
    message = models.TextField()
