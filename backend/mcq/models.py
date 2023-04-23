from django.db import models
from course.models import Subject

# Create your models here.

class Question(models.Model):
    question = models.CharField("question", max_length=5000)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question

class Option(models.Model):
    option = models.CharField("option",max_length=5000)
    is_correct = models.BooleanField("is_correct",default=False)
    question = models.ForeignKey("Question",on_delete=models.CASCADE)

    def __str__(self):
        return self.option

