from django.db import models

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='game_images/')
    details = models.TextField(default='')
    release_date = models.DateTimeField()
    download_link = models.URLField(max_length=200)
