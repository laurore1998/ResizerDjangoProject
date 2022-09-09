from django.db import models
from django.utils import timezone

# Create your models here.

class ImageResize(models.Model):
    time_created = models.DateTimeField(default=timezone.now)
    imagesubmit = models.ImageField(upload_to='dosye_foto/', blank=True, null=True)
    imageresize= models.ImageField(upload_to='dosye_foto/', blank=True, null=True)
    width=models.PositiveIntegerField(default=0)
    heigth = models.PositiveIntegerField(default=0)