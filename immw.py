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
    start_urls = ['https://www.immowelt.de/liste/mannheim/wohnungen/mieten?lat=49.48838&lon=8.50009&sr=50&sort=distance']
    
    
    def parse(self,response):
        print(response)	


# main driver #
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(immowelt)
    process.start()
