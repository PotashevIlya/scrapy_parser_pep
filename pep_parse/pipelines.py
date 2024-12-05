import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import (
    BASE_DIR, DATETIME_FORMAT, RESULTS_DIR_NAME,
    STATUS_SUMMARY_FILENAME
)
from pep_parse.utils import build_dir


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        dir = build_dir(BASE_DIR, RESULTS_DIR_NAME)
        file_path = dir / STATUS_SUMMARY_FILENAME.format(
            now=dt.datetime.now().strftime(DATETIME_FORMAT)
        )
        with open(file_path, 'w', encoding='utf-8') as f:
            print(self.statuses_counter)
            writer = csv.writer(f, dialect=csv.unix_dialect)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.statuses_counter.items())
            writer.writerow(['Всего', sum(self.statuses_counter.values())])
