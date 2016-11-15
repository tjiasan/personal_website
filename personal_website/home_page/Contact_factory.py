import factory
from . import models

class contactFactory(factory.Factory):
    class Meta:
        model= models.Contact
    name = "John Doe"
    email = "John.Doe@mail.com"
    comment = "This is a sample comment"

    
