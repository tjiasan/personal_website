from django.shortcuts import render
from .models import WebContent, BioContent, MachineContent

def web_dev(request, slug):
    template = "project_blog/web_dev_overview.html"
    if slug == "overview":
        content= WebContent.objects.get(category= "Main")
    else:
        content= WebContent.objects.get(slug= slug)
    weblist= WebContent.objects.values('title', 'slug')
    biolist= BioContent.objects.values('title', 'slug')
    machinelist= MachineContent.objects.values('title', 'slug')
    return render (request, template,
                   {'content':content,'weblist':weblist ,'biolist':biolist ,'machinelist':machinelist, 'section': "#webapps", "link": str(content.title),'selector':'projects'},
                   )

def biology(request, slug):
    template = "project_blog/web_dev_overview.html"
    if slug == "overview":
        content= BioContent.objects.get(category= "Main")
    else:
        content= BioContent.objects.get(slug= slug)
 
    weblist= WebContent.objects.values('title', 'slug')
    biolist= BioContent.objects.values('title', 'slug')
    machinelist= MachineContent.objects.values('title', 'slug')
    return render (request, template,
                   {'content':content,'weblist':weblist ,'biolist':biolist ,'machinelist':machinelist, 'section': "#biology", "link": str(content.title),'selector':'projects'},
                   )
def machine(request, slug):
    template = "project_blog/web_dev_overview.html"
    if slug == "overview":
        content= MachineContent.objects.get(category= "Main")
    else:
        content= MachineContent.objects.get(slug= slug)
 
    weblist= WebContent.objects.values('title', 'slug')
    biolist= BioContent.objects.values('title', 'slug')
    machinelist= MachineContent.objects.values('title', 'slug')
    return render (request, template,
                   {'content':content,'weblist':weblist ,'biolist':biolist ,'machinelist':machinelist, 'section': "#machine", "link": str(content.title),'selector':'projects'},
                   )

##def web_dev_main(request):
##    template = "project_blog/web_dev_overview.html"
##    content= WebContent.objects.get(title= "overview")
##    weblist= WebContent.objects.values('title', 'slug')
##    biolist= BioContent.objects.values('title', 'slug')
##    machinelist= MachineContent.objects.values('title', 'slug')
##    
##    return render (request, template,
##                   {'content':content,'weblist':weblist ,'biolist':biolist ,'machinelist':machinelist},
##                   )
##
##def biology_main(request):
##    template = "project_blog/biology_overview.html"
##    content= BioContent.objects.get(title= "overview")
##    return render (request, template, {'content':content}) 
##
##def machine_main(request):
##    template = "project_blog/machine_overview.html"
##    content= MachineContent.objects.get(title= "overview")
##    return render (request, template,{'content':content}) 



# Create your views here.
