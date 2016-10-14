from django.shortcuts import render
from .models import Resume

def resume(request,slug):
    template = "resume/resume.html"
    if slug== "main":
        content = Resume.objects.get(category="Main")
    else:
        content= Resume.objects.get(slug=slug)

    active= str(content.title)
        
    resumelist = Resume.objects.values('title','slug')
    return render (request,template,{'content':content, 'resumelist':resumelist, 'active':active, 'selector':'resume'} )

# Create your views here.
