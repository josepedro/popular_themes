from django.db import models

class Theme(models.Model):
    name =  models.CharField(max_length=200)

class Video(models.Model):
    name =  models.CharField(max_length=200)
    date_uploaded = models.DateTimeField('date uploaded', auto_now_add=True)
    views = models.IntegerField(default=0)
    themes = models.ManyToManyField(Theme)

class Thumb(models.Model):
    is_positive = models.BooleanField()
    time = models.DateTimeField('time thumb', auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Comment(models.Model):
    is_positive = models.BooleanField()
    time = models.DateTimeField('time comment', auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)