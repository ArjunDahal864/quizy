from django.db import models
from course.models import Subject
from authentication.models import User

# Create your models here.

class Question(models.Model):
    question = models.CharField("question", max_length=5000)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question

class Option(models.Model):
    option = models.CharField("option",max_length=5000)
    is_correct = models.BooleanField("is_correct",default=False)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.option

class MCQAnswers(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    option = models.ForeignKey(Option,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email+"'s answer for mcq "+self.question.id
    
