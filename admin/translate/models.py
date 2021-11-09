from django.db import models

# Create your models here.

class Message(models.Model):
    eng_msg = models.CharField(max_length=800)
    morse_msg = models.CharField(max_length=800)
