from django.db import models

# Create your models here.
class ShortenedUrl(models.Model):
    url = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=16, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)