#!/usr/bin/python3

'''


 █████   █████          ████
░░███   ░░███          ░░███
 ░███    ░███   ██████  ░███   ██████
 ░███    ░███  ███░░███ ░███  ███░░███
 ░░███   ███  ░███ ░███ ░███ ░███████
  ░░░█████░   ░███ ░███ ░███ ░███░░░
    ░░███     ░░██████  █████░░██████
     ░░░       ░░░░░░  ░░░░░  ░░░░░░

An amimal who likes to dig.

2025 wookieware..

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0.

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "0.1.1"
__maintainer__ = "Rick Kauffman"
__email__ = "rick@rickkauffman.com"
__status__ = "Alpha"

'''
import requests
from pycentral import NewCentralBase
from utility.get_client_api import get_client
from utility.api_caller import api_caller
import json

def new_site():

    # Build site payload

    api_data = {
        "name": "rick-test222",
        "city": "Gilbert",
        "state": "Arizona",
        "country": "United States",
        "zipcode": "85295",
        "address": "Sesame Street",
        "timezone": {
            "timezoneId": "America/Chicago",
            "timezoneName": "Central Standard Time",
            "rawOffset": -21600000
            }
        }

    client = get_client()

    api_method = "POST"

    api_path="network-config/v1alpha1/sites"

    new_site = api_caller(client,api_method,api_path,api_data)

    print(new_site)

    return

if __name__ == '__main__':
    devices = new_site()
