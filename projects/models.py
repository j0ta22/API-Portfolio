from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
from distutils.command import upload


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = ImageField(upload_to='portfolio/images/')
    image_url = models.CharField(max_length=300)
    url = models.URLField(blank=True)