from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    bunny_proj_id = models.CharField(max_length=30)
    audio_url = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=30)
