from django.db import models
from django.urls import reverse


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def _str_(self):
        return self.album_title + ' _ ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_Type = models.CharField(max_length=10)
    Song_title = models.CharField(max_length=250)

    def _str_(self):
        return self.Song_title

