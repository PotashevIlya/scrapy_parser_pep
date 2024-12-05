import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import (
    DATETIME_FORMAT, STATUS_SUMMARY_FILENAME,
    BASE_DIR, RESULTS_DIR_NAME
)


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR_NAME
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        filename = STATUS_SUMMARY_FILENAME.format(
            now=dt.datetime.now().strftime(DATETIME_FORMAT)
        )
        with open(
            f'{self.results_dir}/{filename}', 'w', encoding='utf-8'
        ) as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows(
                [
                    ('Статус', 'Количество'),
                    *self.statuses_counter.items(),
                    ('Всего', sum(self.statuses_counter.values()))
                ]
            )
