import csv
import datetime as dt

from collections import defaultdict


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_amount_dict = defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.status_amount_dict[status] += 1
        return item

    def close_spider(self, spider):
        format_date = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'results/status_summary_{format_date}.csv'
        with open(
            file_name,
            mode='w',
            newline='',
            encoding='utf-8'
        ) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(('Статус', 'Количеcтво'))
            for status, count in self.status_amount_dict.items():
                writer.writerow((status, count))
            total_status = sum(self.status_amount_dict.values())
            writer.writerow(('Total', total_status))
