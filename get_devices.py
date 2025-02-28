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
from utility.token_info import token_info
import json

def devices():

    client = NewCentralBase(
                token_info=token_info,
                )

    # Get devices with New Central API
    response2 = client.command(
            api_method="GET", api_path="network-monitoring/v1alpha1/devices"
            )
    '''
    # Get devices with glp
    response = client.command(
            api_method="GET", api_path="devices/v1/devices", app_name="glp"
            )
    '''
    devices = response2['msg']['items']

    # Returns a python list of devices
    # return devices

    for d in devices:
        print('__________________________________________________________________')
        print(d)



if __name__ == '__main__':
    devices()
