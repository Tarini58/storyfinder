from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Character(models.Model):
   name = models.CharField(max_length=100)

class Connector(models.Model):
   story = models.ForeignKey(Story, on_delete=models.CASCADE)
   character = models.ForeignKey(Character, on_delete=models.CASCADE)
   
