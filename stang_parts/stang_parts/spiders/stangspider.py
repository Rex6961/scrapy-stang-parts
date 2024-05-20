import os
import sys
from dotenv import load_dotenv

import scrapy
from ..items import StangPartsItem
from ..itemsloaders import StangPartsLoader# Assuming this is your custom item class

load_dotenv()

urls = os.getenv('URLS')
domain = os.getenv('DOMAINS')


class StangPartsSpider(scrapy.Spider):
    """
    Web scraper for Stang Parts website to extract product information
    and save it to an Excel file.

    This spider crawls the Stang Parts website (https://your_example.com)
    and extracts details like title, price, reference number, and availability
    for each car part listed on a product page. It then saves this data
    to an Excel file named "Supplies_for_a_car.xlsx".

    Attributes:
        name (str): Name of the spider for identification within Scrapy.
        allowed_domains (list): List of allowed domains for crawling to prevent
            accidental scraping of external sites.
        start_urls (list): List of starting URLs for the crawl.
    """

    name = "stang_parts"
    allowed_domains = [domain]
    start_urls = [
        urls,  # Starting URL for the crawl
    ]

    def parse(self, response):
        """
        Parses the product information from the given response object.

        Args:
            response (scrapy.http.Response): The response object from Scrapy
                containing the HTML content of the crawled page.

        Yields:
            dict: A dictionary containing the extracted product information
                for each car part on the page.
            scrapy.Request: Requests to follow links for further crawling.
        """

        for item in response.css('article.product-miniature.js-product-miniature'):
            # Extract product information from CSS selectors
            product_items = StangPartsLoader(item=StangPartsItem(), selector=item)
            product_items.add_css('title', "h3.h3.product-title a::text")
            product_items.add_css('price', "span.price::text")
            product_items.add_css('reference', "p.pl_reference strong::text")
            product_items.add_css('availability', "span.pl-availability::text")
            yield product_items.load_item()

        # Follow pagination links and other relevant links for further crawling

        for href in response.css("h5 a.subcategory-name::attr(href)").getall():
            yield response.follow(url=href, callback=self.parse)