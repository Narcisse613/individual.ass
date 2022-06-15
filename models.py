from turtle import title
from django.db import models

# Create your models here.
class Super(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    Technology = models.CharField(max_length=100)
    pub_date = models.DateTimeField('now')
    author = models.CharField(max_length=50)
