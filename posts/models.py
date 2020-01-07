from django.db import models
from django.utils import timezone
import datetime


class Title(models.Model):
    title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Body(models.Model):
    question = models.ForeignKey(Title, on_delete=models.CASCADE)
    body_text = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.body_text