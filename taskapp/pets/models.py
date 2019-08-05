from django.contrib.gis.db import models
import os


def get_image_path():
    return 'pet_photos'


class Pet(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pet_image = models.ImageField(upload_to=get_image_path(), blank=True, null=True)
