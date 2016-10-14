from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from project_blog.views import web_dev, biology, machine
from blog_factory import WebFactory, BioFactory, MachineFactory
from .models import WebContent
from django.core.urlresolvers import reverse

class resolvingtests(TestCase):

    def test_url_resolves_to_main_web_dev(self):
        found = resolve('/projects/web-development/overview')
        self.assertEqual(found.func, web_dev)
        
    def test_url_resolves_to_main_machine(self):
        found = resolve('/projects/machine-learning/overview')
        self.assertEqual(found.func, machine)

    def test_url_resolves_to_biology(self):
        found= resolve('/projects/biology/overview')
        self.assertEqual(found.func, biology)
        
    def test_projects_uses_the_right_template_and_html(self):
        webcon = WebFactory.create()
        biocon= BioFactory.create()
        maccon= MachineFactory.create()

        #save to database
        webcon.save()
        biocon.save()
        maccon.save()
        
        #test web, note: all use the same template
        response = self.client.get(reverse('web_dev', args=(webcon.slug,)))       
        self.assertEqual(response.templates[0].name, "project_blog/web_dev_overview.html")
       
        #test correct content is loaded
        self.assertIn(webcon.content, response.content)

        #machine content loaded
        response =  self.client.get(reverse('machine', args=(maccon.slug,)))  
        self.assertIn(maccon.content, response.content)

        #biology content loaded        
        response =  self.client.get(reverse('biology', args=(biocon.slug,)))  
        self.assertIn(biocon.content, response.content)
        
        #test sidebar loads  titles
        self.assertIn(biocon.title, response.content)
        self.assertIn(maccon.title, response.content)
        self.assertIn(webcon.title, response.content)
        

        
# Create your tests here.
