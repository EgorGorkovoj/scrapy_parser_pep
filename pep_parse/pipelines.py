import csv
import os
import datetime as dt

from collections import defaultdict

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    """
    Класс обработчик. Обрабатывает Items полученный от паука pep.
    Считает количество PEP по статусам и сохраняет итоговую статистику
    в CSV-файл при завершении работы паука.
    """
    def open_spider(self, spider):
        """
        Инициализация перед началом обработки паука.
        Создаёт словарь для подсчёта количества PEP по каждому статусу.
        Параметры:
           1) spider (scrapy.Spider): Экземпляр паука, который запускается.
        """
        self.status_amount_dict = defaultdict(int)

    def process_item(self, item, spider):
        """
        Обрабатывает каждый элемент, подсчитывая статусы.
        Увеличивает счётчик для статуса текущего PEP.
        Параметры:
           1) item (dict): Обрабатываемый элемент с данными PEP;
           2) spider (scrapy.Spider): Паук, который передал элемент.

        Возвращаемое значение:
            item (dict): Передаёт элемент дальше в пайплайн без изменений.
        """
        status = item['status']
        self.status_amount_dict[status] += 1
        return item

    def close_spider(self, spider):
        """
        Завершающий метод — сохраняет статистику по статусам в CSV-файл.
        Файл сохраняется в папку 'results' с текущей датой
        и временем в названии.
        Параметры:
           1) spider (scrapy.Spider): Экземпляр паука,
        который завершил работу.
        """
        format_date = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = BASE_DIR / f'results/status_summary_{format_date}.csv'
        if not os.path.exists(BASE_DIR / 'results'):
            os.makedirs(BASE_DIR / 'results')
        with open(
            file_name,
            mode='w',
            newline='',
            encoding='utf-8'
        ) as csvfile:
            writer = csv.writer(
                csvfile, dialect=csv.unix_dialect, quoting=csv.QUOTE_MINIMAL
            )
            writer.writerow(('Статус', 'Количеcтво'))
            writer.writerows(self.status_amount_dict.items())
            total_status = sum(self.status_amount_dict.values())
            writer.writerow(('Total', total_status))
