import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    """
    Stores a single poll question.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """
    Stores a single choice related to a poll question.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class ChoiceVote(models.Model):
    """
    Stores votes for a poll choice related to :model:`auth.User`.
    """
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    users = models.ManyToManyField(User, related_name='voters')
