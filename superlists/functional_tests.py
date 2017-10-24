from webbrowser import browser

from selenium import webdriver
from unittest import TestCase
import sys



class TestNewVisitor(TestCase):

    def setUp(self):
       self.browser = webdriver.Chrome()
     #  print (sys.version)
  

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
       self.browser.get('http://localhost:8000')
       assert(1 == 2)
