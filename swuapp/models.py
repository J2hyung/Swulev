from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length = 20)
    userpw = models.CharField(max_length = 30)

class UserLecture(models.Model):

    RATING_FIELD = (
        ('on', 'on'),
        ('off', 'off'),
    )

    lectureid = models.ForeignKey('User', on_delete=models.CASCADE, related_name='lectureid', primary_key=True)
    semester = models.CharField(max_length = 30)
    rating = models.CharField(max_length=10, choices=RATING_FIELD, default = "off")