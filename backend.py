import googlemaps
import logging
import json
from time import sleep

class LookupHotelInviumPlaces(object):
    def __init__(self, **kwargs):
        self.logger = logging.getLogger('HotelRefugus')
        self.client = None

    def initialise_places(self, api_key):
        self.client = googlemaps.Client(key=api_key)

    def lookup_hotels(self, address, area, language='en'):
        self.logger.info('Looking up Hotels')
        self.logger.debug(f'Address: {address}\nArea: {area}\nLanguage: {language}')
        coordinates = self.get_gps_coordinates(address)
        response = self.client.places_nearby(location=coordinates,keyword='hotel',
                                             type='lodging',radius=area)
        if response.get('next_page_token') is not None:
            self.logger.debug('More than 20 results found, paging Dr. Token')
            results = response['results']
            page_token = response['next_page_token']
            while page_token is not None:
                try:
                    response = self.client.places_nearby(page_token=page_token)
                except googlemaps.exceptions.ApiError as e: # Requesting page before it's available will trigger this exception so we wait
                    self.logger.debug(e)
                    self.logger.warning('Token is not ready, waiting 2 seconds')
                    sleep(2)
                    response = self.client.places_nearby(page_token=page_token)
                results+=response['results']
                page_token = response.get('next_page_token')

            return results
        else:
            self.logger.info(json.dumps(response['results']))
            return response['results']

    def get_gps_coordinates(self, address):
        response = self.client.geocode(address)
        return '{0},{1}'.format(response[0]['geometry']['location']['lat'],
                                response[0]['geometry']['location']['lng'])