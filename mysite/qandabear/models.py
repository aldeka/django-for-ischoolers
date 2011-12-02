from django.db import models
import datetime

class Question(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.text
        
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    
class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        summary = self.text[:37]
        if len(self.text) > 37:
            summary = summary + '...'
        return summary
