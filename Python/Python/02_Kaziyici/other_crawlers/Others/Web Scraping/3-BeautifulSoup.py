# importing BeautifulSoup form 
# bs4 module 
from bs4 import BeautifulSoup 

# importing requests 
import requests 

# get URL 
r = requests.get("http://www.geeksforgeeks.org") 

data = r.text 
soup = BeautifulSoup(data) 

for link in soup.find_all('a'): 
	print(link.get('href'))