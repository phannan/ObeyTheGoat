from django.urls import resolve
from django.test import TestCase
#from lists.views import home_page

# Create your tests here.
class SmokeTest(TestCase):
    def test_bad_math(self):
        self.assertEqual(1+1,2)

class HomePageTest(TestCase):
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)