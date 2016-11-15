from django.shortcuts import render
from .models import Resume

def resume(request,slug):
    template = "resume/resume.html"
    if slug== "main":
        content = Resume.objects.get(category="Main")
    else:
        content= Resume.objects.get(slug=slug)
    try:
        Next = Resume.objects.only('slug').filter(pk__gt=content.id).order_by('pk')[0].slug
    except:
        Next = None
    try:
        previous = Resume.objects.only('slug').filter(pk__lt=content.id)[0].slug
    except:
        previous = None


    print Next
    print previous
    active= str(content.title)
        
    resumelist = Resume.objects.values('title','slug')
    return render (request,template,{'content':content,
                                     'resumelist':resumelist,
                                     'active':active,
                                     'selector':'resume',
                                     'Next':Next,
                                     'previous':previous

                                     } )

# Create your views here.
