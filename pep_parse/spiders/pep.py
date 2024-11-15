import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        link_peps = response.css('a.pep.reference.internal::attr(href)')
        for link_pep in link_peps:
            yield response.follow(link_pep, callback=self.parse_pep)

    def parse_pep(self, response):
        number = response.css('li:contains("PEP") + li::text').get()
        title_status = response.css('dt:contains("Status") + dd')
        status = title_status.css('abbr::text').get()
        data = {
            'number': number,
            'name': response.css('h1.page-title::text').get(),
            'status': status
        }
        yield PepParseItem(data)
