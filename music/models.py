from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length = 250)
    album_title = models.CharField(max_length = 250)
    genre = models.CharField(max_length = 250)
    album_logo = models.CharField(max_length = 250)

    def __str__(self):
        return 'Album : ' + self.artist + '->' + self.album_title
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    song_title = models.CharField(max_length = 250)
    file_type = models.CharField(max_length = 250)
    isFavorite = models.BooleanField(default = False)

    def __str__(self):
        return "song name is " + self.song_title
