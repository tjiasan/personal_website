from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.http import HttpResponseRedirect
from models import Contact
from django.contrib import messages
import bleach

def home_page(request):

    template = 'home_page/home_page.html'
    
    return render (request, template)


def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form= form.cleaned_data
            name= bleach.clean(form['name'])
            email = bleach.clean(form['email'])
            content= bleach.clean(form['content'])
            new_entry = Contact(name= name, email=email, comment= content)
            new_entry.save()

            
            messages.success(request,"your message has been sucessfully sent")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            errors= form.errors.as_data()
            msg= ""
            for error in errors:
                if error == 'email':
                    msg+= "invalid email"
                if error == 'content':
                    msg +=" content empty"
            messages.error(request,msg)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        form= ContactForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Create your views here.
