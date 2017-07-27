#!/usr/bin/python
import requests
import sys
import csv
import configparser

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

# Creates the meat of the URL
def createurl(row):
    bib_id = row[0]
    holding_id = row[1]
    item_id = row[2]
    return '/almaws/v1/bibs/' + bib_id + '/holdings/'+ holding_id +'/items/' + item_id;

# Reads in the file of items and performs scan in opertion on each item
def read_items(items_file):
    f = open(items_file, 'rt')
    try:
        reader = csv.reader(f)
        next(reader) #skip header line
        for row in reader:
            if row[0] != 'end-of-file':
                apicall = createurl(row)
                query = '?op=scan' + '&library=' + get_library() + '&circ_desk=' + get_circdesk()
                url = get_base_url() + apicall + query
                print (url)
                response = requests.post(url, data={'apikey' : get_key()})
                print (response.content)
    finally:
        f.close()

# Read campus parameters
config = configparser.RawConfigParser()
config.read(sys.argv[1]) # Config file with API key, API URL, circ desk code and library code

items_file = sys.argv[2] # CSV file of items to be checked in
read_items(items_file)
