# https://www.geeksforgeeks.org/python-tools-world-web-scraping/
import mechanicalsoup 
  
browser = mechanicalsoup.StatefulBrowser() 
value = browser.open("http://geeksforgeeks.org/") 
print(value) 
  
value1 = browser.get_url() 
print(value1) 
  
value2 = browser.follow_link("forms") 
print(value2) 
  
value = browser.get_url() 
print(value)