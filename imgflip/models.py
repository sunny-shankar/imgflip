from re import M
from turtle import width
from django.db import models


class MemeModel(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()
    box_count = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.width}x{self.height})"
