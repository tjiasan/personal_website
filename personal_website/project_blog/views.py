from django.shortcuts import render
from .models import WebContent, BioContent, MachineContent

def web_dev_main(request):
    template = "project_blog/web_dev_overview.html"
    content= WebContent.objects.get(title= "overview")
    
    return render (request, template,{'content':content})

def biology_main(request):
    template = "project_blog/biology_overview.html"
    content= BioContent.objects.get(title= "overview")
    return render (request, template, {'content':content}) 

def machine_main(request):
    template = "project_blog/machine_overview.html"
    content= MachineContent.objects.get(title= "overview")
    return render (request, template,{'content':content}) 

def web_dev(request):
    pass

def biology(request):
    pass

def machine(request):
    pass



# Create your views here.
