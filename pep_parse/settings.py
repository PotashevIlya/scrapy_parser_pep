from pathlib import Path

from .utils import build_dir

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
RESULTS_DIR_NAME = 'results'
STATUS_SUMMARY_FILENAME = 'status_summary_{now}.csv'
RESULTS_DIR = build_dir(BASE_DIR, RESULTS_DIR_NAME)

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = SPIDER_MODULES[0]

ROBOTSTXT_OBEY = True

FEEDS = {
    f'{RESULTS_DIR_NAME}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
