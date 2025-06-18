import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """
    Класс PepSpider - 'паук'.
    Собирает информацию о актуальных версиях PEP и их статусах.
    """
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """
        Обрабатывает главную страницу с перечнем PEP.
        Извлекает ссылки на все PEP и запускает для каждой отдельный запрос,
        передавая обработку в метод parse_pep.
        Параметры метода:
            1) response (scrapy.http.Response): Ответ от запроса к start_urls.
        """
        link_peps = response.css('a.pep.reference.internal::attr(href)')
        for link_pep in link_peps:
            yield response.follow(link_pep, callback=self.parse_pep)

    def parse_pep(self, response):
        """
        Обрабатывает страницу отдельного PEP.
        Извлекает номер, название и статус PEP.
        Формирует словарь с данными и отдаёт его
        в пайплайн через объект PepParseItem.
        Параметры метода:
            response (scrapy.http.Response): Ответ от запроса к странице PEP.
        """
        number = response.css('li:contains("PEP") + li::text').get()
        title_status = response.css('dt:contains("Status") + dd')
        status = title_status.css('abbr::text').get()
        data = {
            'number': number,
            'name': response.css('h1.page-title::text').get(),
            'status': status
        }
        yield PepParseItem(data)
