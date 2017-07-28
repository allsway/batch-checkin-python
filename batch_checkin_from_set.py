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

def get_set_id():
    return config.get('Params', 'setid')

# Returns the set ID from the configuration file.  All items in this set will be checked in.
def get_set_url():
    return get_base_url() + '/almaws/v1/conf/sets/' + get_set_id() + '/members?apikey=' + get_key()

# Reads in the file of items and performs scan in opertion on each item
def read_items():
    set_url = get_set_url()
    response = requests.get(set_url)
    if response.status_code == 200:
        members = ET.fromstring(response.content)
        query = '?op=scan' + '&library=' + get_library() + '&circ_desk=' + get_circdesk()
        for member in members.findall('./member'):
            item_url = member.get('link')
            url =  item_url + query
            print (url)
            post_response = requests.post(url, data={'apikey' : get_key()})
            print(post_response.content)


# Read campus parameters
config = configparser.RawConfigParser()
config.read(sys.argv[1]) # Config file with API key, API URL, circ desk code and library code

read_items()
