from django.db import models

# Create your models here.

class Question(models.Model):
    question_test=models.CharField(max_length=200)
    pub_date=models.DateTimeField('data published')

    def __str__(self):
        return str(self.question_test)

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_test=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    
    def __str__(self):
        return str(self.choice_test)