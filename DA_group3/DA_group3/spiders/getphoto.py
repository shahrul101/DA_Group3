
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "pht"

    def start_requests(self):
        urls = [
           'http://172.18.58.238/index.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       css_selector = 'img'
       for x in response.css(css_selector):
           newsel = '@src'
           yield {
               'Image Link': x.xpath(newsel).extract_first(),
           }

       Page_selector = '.next a ::attr(href)'
       next_page = response.css(Page_selector).extract_first()
       if next_page:
           yield scrapy.Request(
               response.urljoin(next_page),
               callback=self.parse
           )
