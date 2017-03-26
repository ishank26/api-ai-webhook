import requests
import json

with open('request.json') as data_file:
    jdata = json.load(data_file)
print jdata

jdata= json.dumps(jdata)
headers = {'content-type': 'application/json'}

r = requests.post('http://0.0.0.0:5000/webhook', data=jdata, headers=headers)

print 'Status: ',r.status_code
print 'JSON: ',r.json()
