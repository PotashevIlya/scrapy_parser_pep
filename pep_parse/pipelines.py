import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import (
    DATETIME_FORMAT, STATUS_SUMMARY_FILENAME, RESULTS_DIR
)


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_path = RESULTS_DIR / STATUS_SUMMARY_FILENAME.format(
            now=dt.datetime.now().strftime(DATETIME_FORMAT)
        )
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows(
                [
                    ('Статус', 'Количество'),
                    *self.statuses_counter.items(),
                    ('Всего', sum(self.statuses_counter.values()))
                ]
            )
