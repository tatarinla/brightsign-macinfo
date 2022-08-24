# -*- coding: utf-8 -*-

import json
import os
import requests
import re
from urllib.parse import urlencode

from exceptions import APIClientError

# Please hardcode your api code here or add it to environment variables
API_KEY = os.environ.get('MACADDRESS_API_KEY')


# Check if mac-address has valid format
def validate_mac_address(func):
    def wrapper(self, mac, *args, **kwargs):
        try:
            if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
                return func(self, mac, *args, **kwargs)
        except:
            return 'Nothing found. Please double-check the mac-address.'
    return wrapper


class APIClient:
    """Communicates with macaddress.io API"""
    __base_url = "https://api.macaddress.io/v1"

    def __init__(self, api_key=API_KEY):
        self.__api_key = api_key

    @validate_mac_address
    def get_full_info(self, mac):

        params = {
            'apiKey': self.__api_key,
            'output': 'json',
            'search': mac
        }

        url = f'{self.__base_url}?{urlencode(params)}'
        data = self.__call(url, method='GET')
        
        return data

    def get_vendor(self, mac):
        try:
            mac_info = self.get_full_info(mac)
            return mac_info['vendorDetails']['companyName']
        except (KeyError, TypeError):
            return 'Cannot find vendor details by the mac-address provided.'

    def __call(self, url, method='GET', data=None):
        try:
            with requests.session() as s:
                s.headers.update({'X-Authentication-Token': self.__api_key})
                if method == 'GET':
                    response = s.get(url)
                elif method == 'POST':
                    response = s.post(url, json=data)
                assert response.status_code == 200

                data = response.json()

        except AssertionError as e:
            raise APIClientError(f'Cannot get response, status code: {response.status_code}')
        
        except ConnectionError as e:
            raise APIClientError('Cannot connect to macaddress.io. Please check your network connection.', str(e))
        
        except requests.Timeout as e:
            raise APIClientError('Cannot get response - times out.', str(e))

        except json.JSONDecodeError as e:
            raise APIClientError('Cannot read response data: ', str(e))

        except Exception as e:
            raise APIClientError('Cannot  get response: ', str(e))

        return data
