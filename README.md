# batch-checkin
Given an Alma item export file, batch check-ins all items from the file using the scan-in item API

###### batch-checkin.py
Takes as arguments
   - initialization file batch-checkin.txt 
   - a csv file from the Alma item export job.  Will check in all items included in the file. 

Run as `python batch-checkin.py batch_checkin.txt items.csv`

###### batch-checkin.txt
Configuration setup can be modified in the file batch-checkin.txt.  Set the check-in library and circulation desk in the batch-checkin.txt file.  
```
[Params]
apikey: apikey 
baseurl: https://api-na.hosted.exlibrisgroup.com
library: librarycode
circdesk: circdeskcode
```
