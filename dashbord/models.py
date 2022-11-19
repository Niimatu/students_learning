from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return f'{self.title} -{self.user} -- Notes'
    
    
class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    body = models.TextField() 
    due = models.DateTimeField(verbose_name="date")
    done = models.BooleanField(default=False)  
    
    
    def __str__(self):
        return f'{self.title} -{self.user} -- Home work'
    
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    is_finish = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title} - {self.user} --Todo'
    

    
    
