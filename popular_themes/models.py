from django.db import models

def validate_date(date):
    if date.year - datetime.now.year != 0:
       raise ValidationError(
        _('video have more than 1 year old'),
    )

class Theme(models.Model):
    name =  models.CharField(max_length=200)
    class Meta:
        ordering = ['name']
    def __unicode__(self):
        return self.name

class Video(models.Model):
    name =  models.CharField(max_length=200)
    date_uploaded = models.DateTimeField('date uploaded', validators=[validate_date])
    views = models.IntegerField(default=0)
    themes = models.ManyToManyField(Theme)
    class Meta:
        ordering = ['name']
    def __unicode__(self):
        return self.name

class Thumb(models.Model):
    is_positive = models.BooleanField()
    time = models.DateTimeField('time thumb')
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Comment(models.Model):
    is_positive = models.BooleanField()
    time = models.DateTimeField('time comment')
    video = models.ForeignKey(Video, on_delete=models.CASCADE)