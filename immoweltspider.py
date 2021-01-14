# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


import scrapy
import os
from scrapy.crawler import CrawlerProcess
from scrapy import Request

class immowelt(scrapy.Spider):

    name = 'immoweltspider'
    start_urls = ['https://www.immowelt.de/liste/mannheim/wohnungen/mieten']
    
    # query string parameters
    params = {
    'query': 'geoid%3D10808222000%26etype%3D1%26esr%3D2',
    'offset': 8,
    'pageSize': 4
    }
    
    
    def parse(self,response):
        print(response)	
        
        
      
