from django.db import models
from django.contrib.auth.models import User
DIFFICULTY_CHOICES = (('EASY', 'EASY'), ('MEDIUM', 'MEDIUM'), ('HARD', 'HARD'))
class Quiz(models.Model):
    name = models.CharField(max_length=60)
    topic = models.CharField(max_length=100)
    number_of_questions = models.PositiveIntegerField()
    time_of_questions = models.PositiveIntegerField()
    required_score_to_pass = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=60, choices=DIFFICULTY_CHOICES)
# Create your models here.
