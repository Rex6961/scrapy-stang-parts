# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StangPartsItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    reference = scrapy.Field()
    availability = scrapy.Field()
