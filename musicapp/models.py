from email.policy import default
# from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    age = models.IntegerField()

    def get_user_name(self):
        return self.first_name


class Song(models.Model):
    
    title = models.CharField(max_length=50)
    date_released = models.DateField(default=datetime.today)
    likes = models.PositiveIntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete = models.PROTECT)

    def get_title(self):
        return self.title

class Lyrics(models.Model):
     
    content = models.TextField()
    song_id =models.ForeignKey(Song, on_delete = models.PROTECT)

    def get_lyric(self):
        return self.content

