import requests
import json
import datetime
apikey = 'sPYngrqc3a29GkMAd2SOBDuPm7VdHT9o'
headers={'key':apikey}

endpoint = 'https://app.ticketmaster.eu/mfxapi/v1/'


par={u'name':'value1'}
resp=requests.get('https://app.ticketmaster.com/discovery/v2/events.json?size=20&keyword=post_malone&sort=relevance,desc&apikey=sPYngrqc3a29GkMAd2SOBDuPm7VdHT9o',params=par)
response=resp.text
jsonresp = resp.json()
for i in range(0,len(jsonresp.get(u'_embedded').get(u'events'))):
    for j in range(0,len(jsonresp.get(u'_embedded').get(u'events')[i].get(u'dates').get(u'start').get(u'localDate'))):
        

with open('data.txt', 'w') as outfile:
    json.dump(jsonresp, outfile)
if resp.status_code != 200:
    print"error"
