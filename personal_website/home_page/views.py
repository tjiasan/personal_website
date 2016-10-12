from django.shortcuts import render, get_object_or_404



def home_page(request):

    template = 'home_page/home_page.html'
    
    return render (request, template) 

# Create your views here.
