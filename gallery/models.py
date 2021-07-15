from datetime import date
from django.db import models
from django.contrib.auth import get_user_model
from user.models import User

class Photo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    caption = models.CharField(max_length=200, null=True, blank=True)
    image_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name_plural = "Photos"
        verbose_name = "Photo"


class Album(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=date.today)
    description = models.TextField(null=True, blank=True)
    photos = models.ManyToManyField(Photo, related_name='album')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Albums"
        verbose_name = "Album"
