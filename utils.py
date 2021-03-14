from datetime import datetime, timedelta

domain_codes = {
    'b': 'wikibooks',
    'd': 'wiktionary',
    'f': 'wikimediafoundation',
    'm': 'wikipedia',
    'n': 'wikinews',
    'q': 'wikiquote',
    's': 'wikisource',
    'v': 'wikiversity',
    'voy': 'wikivoyage',
    'w': 'mediawiki',
    'wd': 'wikidata'
}


class line:
    def __init__(self, text):
        values = text.split(' ')
        self.domain_code = values[0]
        self.page_title = values[1]
        self.view_count = int(values[2])


class landom:
    def __init__(self, language, domain):
        self.language = language
        self.domain = domain


def subtract_hours(datetime, hours):
    delta = timedelta(hours=hours)
    return datetime - delta


def generate_url(datetime):
    year = datetime.year
    month = datetime.month
    day = datetime.day
    hour = datetime.hour

    return f'https://dumps.wikimedia.org/other/pageviews/{year}/{year}-{month:02d}/pageviews-{year}{month:02d}{day:02d}-{hour:02d}0000.gz'


def parsePeriod(hour):
    if 0 <= hour <= 23:
        if hour > 12:
            return f'{hour - 12}PM'
        elif hour == 12:
            return '12PM'
        else:
            return f'{hour}AM'
    else:
        return ''


def parse_landom(domain_code):
    values = domain_code.split('.')
    ld = landom(values[0], domain_codes[values[-1]])
    return ld
