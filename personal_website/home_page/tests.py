from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from home_page.views import home_page
from Contact_factory import contactFactory
from django.test.utils import setup_test_environment
from .models import Contact


class Test1(TestCase):

    def test_root_url_resolves_to_home_age_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request =HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title> Jason Alexander Lee </title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


class FormTest(TestCase):
    
    
  
    def test_contact_form_can_receive_good_data(self):
        contact= contactFactory.build()
        response= self.client.post('/contact/', {'name': contact.name, 'email': contact.email, 'content':contact.comment})
        self.assertEqual(response.status_code, 302)
        new_contact = Contact.objects.get(pk=1)
        self.assertEqual(new_contact.name, "John Doe")

    def test_contact_form_does_not_save_bad_data(self):
        contact= contactFactory.build(email = "badmail")
        response= self.client.post('/contact/', {'name': contact.name, 'email': contact.email, 'content':contact.comment})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Contact.objects.all().exists())
        

        
    
        

        
         


        
        
        
# Create your tests here.
