from datetime import datetime
import os
import requests
import gzip
import shutil

import utils

dl_path = 'tmp/'
limit = 5
now = datetime.utcnow()
landom = []
pagecount = []


if not os.path.exists(dl_path):
    os.mkdir(dl_path)

for x in range(1, limit + 1):
    dt = utils.subtract_hours(now, x)
    url = utils.generate_url(dt)
    filename = url.split('/')[-1]
    headname = filename.split('.')[0]

    if not os.path.exists(f'{dl_path}{filename}') and not os.path.exists(f'{dl_path}{headname}'):
        gz_file = requests.get(url)
        open(f'{dl_path}{filename}', 'wb').write(gz_file.content)

    if not os.path.exists(f'{dl_path}{headname}'):
        with gzip.open(f'{dl_path}{filename}', 'rb') as f_in:
            with open(f'{dl_path}{headname}', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                os.remove(f'{dl_path}{filename}')

    with open(f'{dl_path}{headname}', 'r') as readable:
        lines = set(readable.readlines())

    max_landom = None
    max_pagecount = 0
    page_title = dict()

    for text in lines:
        if text.split(' ').__len__() == 4:
            line = utils.line(text)

        if max_landom == None or max_landom.view_count < line.view_count:
            max_landom = line

        if line.page_title in page_title:
            page_title[line.page_title] += line.view_count
        else:
            page_title[line.page_title] = line.view_count

    ld = utils.parse_landom(max_landom.domain_code)

    landom.append(
        f'{utils.parsePeriod(dt.hour):<20}{ld.language:<20}{ld.domain:<20}{max_landom.view_count:<20}')

    index = ''

    for key in page_title:
        if max_pagecount < page_title[key]:
            max_pagecount = page_title[key]
            index = key

    pagecount.append(
        f'{utils.parsePeriod(dt.hour):<20}{index:<20}{page_title[index]:<20}')

prd = 'Period'
lng = 'Language'
dmn = 'Domain'
vwcnt = 'ViewCount'
landom.append(f'{prd:<20}{lng:<20}{dmn:<20}{vwcnt:<20}')
landom.reverse()

for x in landom:
    print(x)

print('\n')

pg = 'Page'
pagecount.append(f'{prd:<20}{pg:<20}{vwcnt:<20}')
pagecount.reverse()

for x in pagecount:
    print(x)
