import logging
import os
import json
from backend import LookupHotelInviumPlaces

API_KEY = os.environ.get('API_KEY')
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL')

def handler(event, context):
    if LOGGING_LEVEL == 'DEBUG':
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)
    logging.info('Received Address Lookup Request')
    logging.info(json.dumps(event))
    places = LookupHotelInviumPlaces()
    places.initialise_places(api_key=API_KEY)
    request = json.loads(event['body'])
    address = request['address']
    language = request.get('language', 'en')
    area = request['area']

    return {
        "statusCode": 200,
        "body": json.dumps(places.lookup_hotels(address=address, language=language, area=area)),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    }
