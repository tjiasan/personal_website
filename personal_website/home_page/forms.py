from  django import forms

class ContactForm (forms.Form):
    name = forms.CharField(label= "Name", max_length =100)
    email= forms.EmailField()
    content= forms.CharField(label= "Content", max_length=1000)
    
    
