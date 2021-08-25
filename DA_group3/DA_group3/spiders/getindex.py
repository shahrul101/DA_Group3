import scrapy


class QuotesSpider(scrapy.Spider):
    name = "ind"

    def start_requests(self):
        urls = [
           'http://172.18.58.238/index.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'ind.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
