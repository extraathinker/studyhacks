from django.db import models
from autoslug import AutoSlugField

class newPost(models.Model):
    title = models.CharField(max_length=50)
    titleSlug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    postImg = models.FileField(upload_to='images/',max_length=250,null=True,default=None)
    description = models.TextField()

# Create your models here.
