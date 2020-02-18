import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

AIRTABLE_CONFIG_FILE = os.getenv('PROPPER_AIRTABLE_CONFIG_FILE', os.path.join(BASE_DIR, 'env/airtable.json'))

assert os.path.isfile(AIRTABLE_CONFIG_FILE)
with open(AIRTABLE_CONFIG_FILE, 'r') as fd:
    AIRTABLE_CONFIG = json.loads(fd.read())
