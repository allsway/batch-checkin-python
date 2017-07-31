#!/usr/bin/python
import requests
import sys
import configparser
import xml.etree.ElementTree as ET

# Returns the API key
def get_key():
    return config.get('Params', 'apikey')

# Returns the Alma API base URL
def get_base_url():
    return config.get('Params', 'baseurl')

# Returns the circ desk code that will perform the item checkin
def get_circdesk():
    return config.get('Params','circdesk')

# Returns the library code for the library performing the item checkin
def get_library():
    return config.get('Params','library')

# Returns the ID number for the set of items to be scanned in.  You can get this from the Manage Sets | Edit screen.
def get_set_id():
    return config.get('Params', 'setid')

# Returns the set ID from the configuration file.  All items in this set will be checked in.
def get_set_url():
    return get_base_url() + '/almaws/v1/conf/sets/' + get_set_id() + '/members?apikey=' + get_key()

# Reads in the file of items and performs scan in opertion on each item
def read_items():
    limit = 100
    response = requests.get(get_set_url())
    if response.status_code == 200:
        members = ET.fromstring(response.content)
        total_in_set = int(members.get('total_record_count'))
        offset = 0
        for x in range(offset,total_in_set):
            query = '?op=scan' + '&library=' + get_library() + '&circ_desk=' + get_circdesk()
            for member in members.findall('./member'):
                item_url = member.get('link')
                url =  item_url + query
                post_response = requests.post(url, data={'apikey' : get_key()})
                print(post_response.content)
            offset += limit

# Read campus parameters
config = configparser.RawConfigParser()
config.read(sys.argv[1]) # Config file with API key, API URL, circ desk code and library code

read_items()
