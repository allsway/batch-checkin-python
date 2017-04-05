#!/usr/bin/python
import requests
import sys
import csv
import configparser
import xml.etree.ElementTree as ET

def createurl(row):
	bib_id = row[0]
	holding_id = row[1]
	item_id = row[2]
	return '/almaws/v1/bibs/' + bib_id + '/holdings/'+ holding_id +'/items/' + item_id; 

# Read campus parameters
config = configparser.RawConfigParser()
config.read(sys.argv[1])
apikey = config.get('Params', 'apikey')
baseurl = config.get('Params','baseurl')
library = config.get('Params','library')
circdesk = config.get('Params','circdesk')

# CSV file of items to be checked in
items_file = sys.argv[2]
query = '?op=scan' + '&library=' + library + '&circ_desk=' + circdesk


f = open(items_file, 'rt')
try:
    reader = csv.reader(f)
    next(reader)#skip header line
    for row in reader:
    	if row[0] != 'end-of-file':
    		apicall = createurl(row)
    		url = baseurl + apicall + query
    		print (url)
    		response = requests.post(url, data={'apikey' : apikey})
    		print (response.content)
finally:
    f.close()
	







