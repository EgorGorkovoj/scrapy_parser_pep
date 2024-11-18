import scrapy


class PepParseItem(scrapy.Item):
    """Класс для сохранения объектов, полученных при парсинге."""
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
