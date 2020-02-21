import os
import time

from mbvk import MBVKAuction
from airtable import Airtable
from settings import *

airtable = Airtable(AIRTABLE_CONFIG['db'], AIRTABLE_CONFIG['table'], api_key=AIRTABLE_CONFIG['apiKey'])
auctionAPI = MBVKAuction()

while True:
    print('Polling ...')
    for airRecord in airtable.get_all(formula="AND({Végrehajtási ügyszám}!='', {Minimum ár}='', {Tries}<4)", fields=['Végrehajtási ügyszám', 'TRIES']):
        auctions = auctionAPI.get([airRecord["fields"]['Végrehajtási ügyszám']])
        print('=====================================')

        # Basic error handling
        if len(auctions) == 0:
            print(f'Warning: Record not found in MBVK database [{airRecord}]')
            airtable.update(airRecord['id'], {'TRIES': int(airRecord["fields"]['TRIES']) + 1})
            continue

        auction = auctions[0]

        imageLinks = []
        for image in auction['images']:
            imageLinks.append({
                'url': image
            })
        record = {
            'Images': imageLinks,
            'TRIES': 0,
            **auction['details']
        }
        print('Info: Update record in db ...')
        print(record)
        airtable.update(airRecord['id'],  record)

    time.sleep(10)
