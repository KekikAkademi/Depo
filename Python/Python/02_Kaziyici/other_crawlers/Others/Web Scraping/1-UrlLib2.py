# Using urllib2 module 
from urllib.request import urlopen 
  
html = urlopen("http://geeksforgeeks.org") 
  
print(html.read())