import scrapy
from tutorial.items import AFLItem

class AFL_wiki_Spider(scrapy.Spider):
    name = "AFL-wiki"
    start_urls = [
        "https://en.wikipedia.org/wiki/Australian_Football_League#Current_clubs"
    ]
    def parse(self,response):
        sel = response.xpath('//table[preceding-sibling::h3/span[@id="Current_clubs"] and following-sibling::h3/span[@id="Former_clubs"]]')[0]
        #This would point toward the table below Current clubs and above former clubs
        print("--------------------------------")
        for row in sel.xpath('tr'):
            print(row.extract())
        print("--------------------------------")
