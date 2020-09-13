# Using requests module 
import requests 
  
# get URL 
req = requests.get('http://www.geeksforgeeks.org/') 
  
print(req.encoding)      
print(req.status_code)  
print(req.elapsed)      
print(req.url)          
print(req.history)      
print(req.headers['Content-Type'])