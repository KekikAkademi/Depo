# importing scrapy module 
import scrapy 
  
class GeeksSpider(scrapy.Spider): 
      
    name = "geeks_spider"
      
    start_urls = ['http://www.geeksforgeeks.org'] 
      
    # Parse function 
    def parse(self, response): 
          
        SET_SELECTOR = 'geeks'
        for geek in response.css(SET_SELECTOR): 
            pass