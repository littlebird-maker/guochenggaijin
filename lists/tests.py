#from django.test import TestCase

#class SmokeTest(TestCase):
#    def test_bad_maths(self):
#        self.assertEqual(1+1,3)
## Create your tests here.

from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
        
    #def test_root_url_resolve_to_home_page_view(self):
    #    found=resolve('/')
    #    self.assertEqual(found.func,home_page)
    #def test_home_page_returns_correct_html(self):
    #    #request=HttpRequest()
    #    #response=home_page(request)
    #    response=self.client.get('/')
        
    #    html=response.content.decode('utf8')
    #    self.assertTrue(html.startswith('<html>'))
    #    self.assertIn('<title>To-Do list</title>',html)
    #    self.assertTrue(html.strip().endswith('</html>'))
        
    #    self.assertTemplateUsed(response,'wrong.html')