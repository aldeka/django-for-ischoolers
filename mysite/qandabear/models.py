from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
