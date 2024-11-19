import csv
import os
import datetime as dt

from collections import defaultdict

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    """Класс обработчик. Обрабатывает Items полученный от паука pep."""
    def open_spider(self, spider):
        self.status_amount_dict = defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.status_amount_dict[status] += 1
        return item

    def close_spider(self, spider):
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
