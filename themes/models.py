from django.db import models

# Create your models here.
class SiteSettig(models.Model):
    banner=models.ImageField(upload_to='SiteSettig')
    caption=models.TextField()
