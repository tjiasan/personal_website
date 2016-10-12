from __future__ import unicode_literals
from django.template.defaultfilters import slugify

from django.db import models



class WebContent(models.Model):
    category= models.CharField(max_length=100,null=False)
    title = models.CharField(max_length=500,null=False)
    content = models.CharField(max_length=10000)
    slug = models.SlugField()
    def save (self,*args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(WebContent, self).save(*args, **kwargs)

class BioContent(models.Model):
    category= models.CharField(max_length=100,null=False)
    title = models.CharField(max_length=500,null=False)
    content = models.CharField(max_length=10000)
    slug = models.SlugField()
    def save (self,*args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(BioContent, self).save(*args, **kwargs)
    
class MachineContent(models.Model):
    category= models.CharField(max_length=100,null=False)
    title = models.CharField(max_length=500,null=False)
    content = models.CharField(max_length=10000)
    slug = models.SlugField()
    def save (self,*args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(MachineContent, self).save(*args, **kwargs)
##    def __str__(self):
##        return self.BlogContent.title
    
    

