from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=250)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice = models.CharField(max_length=100)
    vote_tally = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
