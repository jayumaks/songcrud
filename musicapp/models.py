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


class Song(models.Model):
    Artist = models.ForeignKey(Artiste, on_delete = models.PROTECT)
    title = models.CharField(max_length=50)
    date_released = models.DateField(default=datetime.today)
    likes = models.PositiveIntegerField()
    artiste_id = models.IntegerField()

class Lyrics(models.Model):
    Song  = models.ForeignKey(Song, on_delete = models.PROTECT)
    content = models.TextField()
    song_id = models.IntegerField()

