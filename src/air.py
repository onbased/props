import os

from mbvk import MBVKAuction
from airtable import Airtable
from settings import *

airtable = Airtable(AIRTABLE_CONFIG['db'], AIRTABLE_CONFIG['table'], api_key=AIRTABLE_CONFIG['apiKey'])
auctionAPI = MBVKAuction()

for auction in auctionAPI.get(['017.V.1118/2017/69']):
    imageLinks = []
    for image in auction['images']:
        imageLinks.append({
            'url': image
        })
    record = {
        'Images': imageLinks,
        **auction['details']
    }
    print('=====================================')
    print('Inserting record to db ...')
    print(record)
    airtable.insert(record)
