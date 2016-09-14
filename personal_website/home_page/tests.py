from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from home_page.views import home_page

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
# Create your tests here.
