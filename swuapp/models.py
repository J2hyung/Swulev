from django.db import models


class User(models.Model):
    userid = models.CharField(max_length = 20,primary_key=True,unique=True, null=False)
    userpw = models.CharField(max_length = 30)

class UserLecture(models.Model):
    RATING_FIELD = (
        ('on', 'on'),
        ('off', 'off'),
    )
    l_userid = models.ForeignKey('User', on_delete=models.CASCADE, related_name='l_userid', unique=True,null=False,primary_key=True)
    l_lectureid = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name='l_lectureid', unique=True)

class Lecture(models.Model):
    semester = models.CharField(max_length = 30)
    lectureid = models.CharField(max_length=20, primary_key=True)
    lecturename = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)

class Board(models.Model):
    boardid = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=100)
    qualityscore = models.IntegerField()
    difficultyscore = models.IntegerField()
    recommendation = models.IntegerField()
    declaration = models.IntegerField()
    b_userid =  models.ForeignKey('User', on_delete=models.CASCADE, related_name='b_userid', unique=True)
    b_lectureid = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name='b_lectureid', unique=True)

    
