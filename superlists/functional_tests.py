from webbrowser import browser

from selenium import webdriver
from unittest import TestCase

#browser = webdriver.Chrome()
#browser.get('http://phannan.pythonanywhere.com')
#import os
#print (os.environ['PATH'])
import sys


# assert 'To-Do' in browser.title, "RED:  Browser title was " + browser.title

class TestNewVisitor(TestCase):

    def setUp(self):
       self.browser = webdriver.Chrome()
       print (sys.version)
     #  self.id()

    def tearDown(self):
        self.browser.quit()
    #   self.id()

    def test_can_start_a_list_and_retrieve_it_later(self):
       # browser.get('http://phannan.pythonanywhere.com')
       self.browser.get('http://localhost:8000')
 #      assert(1 == 1)
       self.assertIn ('To-Do',self.browser.title)
       self.fail('FINISH THIS')