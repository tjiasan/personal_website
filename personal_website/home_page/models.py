from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=250, null= False)
    email = models.EmailField(null= False)
    comment = models.CharField(max_length=1500, null= False)

##    def __str__(self):
##        return self.Contact.name 

# Create your models here.
