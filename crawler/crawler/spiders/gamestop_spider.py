#Author: Sanjeewa B. Senanayaka
#Gamestop Crawler: Scrapes title, console, publisher, price, rating, condition

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import html

class QuotesSpider(CrawlSpider):
    name = "gamestop"
    allowed_domains = ["gamestop.com"]
    start_urls = [
        'https://www.gamestop.com/browse/games?nav=28-xu0,13ffff2418',

    ]

    rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="next_page"]',)), callback="parse_page", follow=True),)

    def parse_page(self, response):
        container = response.xpath("//div[@class='products']")
        for item1 in container.xpath(".//div[@class= 'product new_product']"):
            print("-----------------------NEW PRODUCT----------------------")
            yield {
                'title': item1.xpath(".//a[@class='ats-product-title-lnk']/text()").extract_first(),
                'console':item1.xpath(".//h3/strong/text()").extract_first(),
                'publisher': item1.xpath(".//p[@class='publisher ats-product-publisher']/text()").extract_first(),
                'price': item1.xpath(".//p[@class='pricing ats-product-price']/text()").extract_first(),
                'rating': item1.xpath(".//div[@class='rating ats-searchMob-prodRating']/@data-rating").extract_first(),
                'condition': "New Product",
            }
        for item2 in container.xpath(".//div[@class= 'product preowned_product']"):
            print("---------------------PRE OWNED------------------------")
            yield {
                'title': item2.xpath(".//a[@class='ats-product-title-lnk']/text()").extract_first(),
                'console':item2.xpath(".//h3/strong/text()").extract_first(),
                'publisher': item2.xpath(".//p[@class='publisher ats-product-publisher']/text()").extract_first(),
                'price': item2.xpath(".//p[@class='pricing ats-product-price']/text()").extract_first(),
                'rating': item2.xpath(".//div[@class='rating ats-searchMob-prodRating']/@data-rating").extract_first(),
                'condition': "Pre-owned",
            }
        for item3 in container.xpath(".//div[@class= 'product digital_product']"):
            print("---------------------DIGITAL------------------------")
            yield {
                'title': item3.xpath(".//a[@class='ats-product-title-lnk']/text()").extract_first(),
                'console':item3.xpath(".//h3/strong/text()").extract_first(),
                'publisher': item3.xpath(".//p[@class='publisher ats-product-publisher']/text()").extract_first(),
                'price': item3.xpath(".//p[@class='pricing ats-product-price']/text()").extract_first(),
                'rating': item3.xpath(".//div[@class='rating ats-searchMob-prodRating']/@data-rating").extract_first(),
                'condition': "Download",
            }
