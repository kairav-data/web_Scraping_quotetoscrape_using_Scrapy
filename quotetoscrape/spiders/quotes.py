import scrapy
from ..items import QuotetoscrapeItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):

        for quote in response.css("div.quote"):
            items = QuotetoscrapeItem()

            items["text"] = quote.css("span.text::text").get()
            items["author"] = quote.css("small.author::text").get()
            items["tags"] = quote.css("div.tags a.tag::text").getall()


            yield items
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

