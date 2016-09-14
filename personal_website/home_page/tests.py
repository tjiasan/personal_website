from django.test import TestCase
from django.core.urlresolvers import resolve
from home_page.views import home_page

class Test1(TestCase):

    def test_root_url_resolves_to_home_age_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
# Create your tests here.
