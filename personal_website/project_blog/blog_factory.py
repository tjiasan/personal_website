import factory
from . import models

class WebFactory(factory.Factory):
    class Meta:
        model= models.WebContent
    category= "Main"
    title = "overview"
    content = "Web content"
    slug = "blablablab"

class BioFactory(factory.Factory):
    class Meta:
        model= models.BioContent
    category= "Main"
    title = "overview"
    content = "Biology content"
    slug = "blablablab"

class MachineFactory(factory.Factory):
    class Meta:
        model= models.MachineContent
    category= "Main"
    title = "overview"
    content = "Machine content"
    slug = "blablablab"

    
