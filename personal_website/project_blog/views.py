from django.shortcuts import render

def web_dev_main(request):
    template = "project_blog/web_dev_overview.html"
    return render (request, template)

def biology_main(request):
    template = "project_blog/biology_overview.html"
    return render (request, template) 

def machine_main(request):
    template = "project_blog/machine_overview.html"
    return render (request, template) 


# Create your views here.
