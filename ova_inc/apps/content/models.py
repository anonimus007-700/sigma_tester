from django.db import models

from django.contrib.auth.models import User

class Tests(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Question(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    question_text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    istrue = models.BooleanField()

class Check(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
