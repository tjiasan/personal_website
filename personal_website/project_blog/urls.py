"""personal_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
 #project blog overview URL
    url(r'^web-development/overview$', views.web_dev_main  ,name= 'web_dev'),
    url(r'^biology/overview$', views.biology_main  ,name= 'biology'),
    url(r'^machine-learning/overview$', views.machine_main  ,name= 'machine'),
 #project blog subheading URLs
    url(r'^web-development/(?P<web_id>[0-9]+)-(?P<web_title>[abc]+)$', views.web_dev_main  ,name= 'web_dev_sub'),
    url(r'^biology/(?P<bio_id>[0-9]+)-(?P<biology_title>[abc]+)$', views.biology_main  ,name= 'biology_sub'),
    url(r'^machine-learning/(?P<machine_id>[0-9]+)$-(?P<machine_title>[abc]+)', views.machine_main  ,name= 'machine_sub'),
]
##
##
##
