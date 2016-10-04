#!/usr/bin/python
import requests
import sys
import csv
import xml.etree.ElementTree as ET

apikey = "l7xx99bfe8556330412ca0df66d724e8cbf6"
baseurl = "https://api-na.hosted.exlibrisgroup.com"
campuscode =  "01CALS_UHL"
library = "CSUEB-CIRC"
circdesk = "DEFAULT_CIRC_DESK"

items_file = sys.argv[1] #Item csv file for checking in
query = '?op=scan' + '&library=' + library + '&circ_desk=' + circdesk



f = open(items_file, 'rt')
try:
    reader = csv.reader(f)
    reader.next() #skip header line
    for row in reader:
    	if row[0] != 'end-of-file':
			bib_id = row[0]
			holding_id = row[1]
			item_id = row[2]
			url =  baseurl + '/almaws/v1/bibs/' + bib_id + '/holdings/'+ holding_id +'/items/' + item_id + query
			print url
			response = requests.post(url, data={ 'apikey' : apikey})
			print response.content
finally:
    f.close()
	
