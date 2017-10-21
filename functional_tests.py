from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://phannan.pythonanywhere.com')
assert 'Django' in browser.title