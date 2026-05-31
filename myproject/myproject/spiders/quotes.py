import scrapy

class QuotesSpider(scrapy.Spider):

    name = "quotes"

    start_urls = [
        "http://quotes.toscrape.com"
    ]

    def parse(self, response):

        quotes = response.css("div.quote")

        for q in quotes:

            yield {
                "quote": q.css("span.text::text").get(),
                "author": q.css("small.author::text").get()
            }

        next_page = response.css("li.next a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)