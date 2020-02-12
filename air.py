import os

from airtable import Airtable

airtable = Airtable('appc6a3oA3jmgB3TG', 'tblXVowNDPY3M3eNi', api_key=os.getenv('AIRTABLE_APIKEY', ''))
print(airtable.get_all(maxRecords=20))
