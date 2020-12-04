
from selenium import webdriver                         
browser = webdriver.Chrome(r'C:\python\chromedriver.exe')

for i in range(50):
    browser.get("http://www.askmap.net")
