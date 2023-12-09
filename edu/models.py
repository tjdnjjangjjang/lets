from django.db import models

# Create your models here.
class feed(models.Model):
    content = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='image/', max_length=255, null=True, blank=True)