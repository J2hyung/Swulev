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

    myuserid = models.ForeignKey('User', on_delete=models.CASCADE, related_name='myuserid', unique=True,primary_key=True)
    mylectureid = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name='mylectureid')
    mysemester = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name='mysemester')
    rating = models.CharField(max_length=10, choices=RATING_FIELD, default = "off")

class Lecture(models.Model):
    lectureid = models.CharField(max_length=20, primary_key=True)
    lecturename = models.CharField(max_length=30)
    professor = models.CharField(max_length=20)
    semester = models.CharField(max_length = 30)