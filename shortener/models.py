from django.db import models

from .utils import code_generator

SHORTCODE_SIZE = 6

# Create your models here.
class ShortenedUrl(models.Model):
    url = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=16, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = code_generator(SHORTCODE_SIZE)
        super().save(*args, **kwargs)    