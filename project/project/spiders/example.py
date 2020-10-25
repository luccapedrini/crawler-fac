import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        url = 'http://www.tjes.jus.br/category/s1-front-page/ultimasnoticias/'
        yield scrapy.Request(url, self.parse)

    def parse(self, response, **kwargs):
        for news in response.css('div.caption'):
            yield {
                'title': news.css('a.article-titulo h2::text').get(),
                'desc': news.css('div.intro-text p::text').get(),
                'url': news.css('a.article-titulo::attr(href)').get()
            }