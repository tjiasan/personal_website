from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models

class Resume(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=100)
    def save (self,*args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Resume, self).save(*args, **kwargs)
    

# Create your models here.
