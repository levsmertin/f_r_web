from django.db import models
from django.utils import timezone

class PhotoBase(models.Model):
    photo = models.ImageField(upload_to='Photos1')
    text1 = models.CharField(max_length=200, null=True, blank=True)
    text22= models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.id)
