from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from project_blog.views import .

class Test2(TestCase):

    def test_url_resolves_to_home(self):
        found = resolve('/projects/web/overview')
        self.assertEqual(found.func, web_dev_main)


# Create your tests here.
