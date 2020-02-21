from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length = 20)
    userpw = models.CharField(max_length = 30)
    