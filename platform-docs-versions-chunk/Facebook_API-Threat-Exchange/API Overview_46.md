platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/examples


## Python

Example 1: A query to get all threat indicators which are IP Addresses of proxies in ThreatExchange.

import requests
import json
import ast
import urllib

app\_id = '555' # Replace this with your app ID
app\_secret = '1234' # Replace this with your app secret
type\_ = 'IP\_ADDRESS'
text = 'proxy'

query\_params = urllib.urlencode({
'access\_token' : app\_id + '|' + app\_secret,
'type' : type\_,
'text' : text
})

r = requests.get('https://graph.facebook.com/v2.4/threat\_indicators?' + query\_params)

print json.dumps(ast.literal\_eval(r.text), sort\_keys=True,indent=4,separators=(',', ': '))

Example 2: A query to get all IP Addresses of proxies uploaded by the Facebook Administrator app in ThreatExchange.

import requests
import json
import ast
import urllib

app\_id = '555' # Replace this with your app ID
app\_secret = '1234' # Replace this with your app secret
type\_ = 'IP\_ADDRESS'
owner\_app\_id = 820763734618599
text = 'proxy'

query\_params = urllib.urlencode({
'access\_token' : app\_id + '|' + app\_secret,
'type' : type\_,
'owner' : owner\_app\_id,
'text' : text
})

r = requests.get('https://graph.facebook.com/v2.4/threat\_descriptors?' + query\_params)

print json.dumps(ast.literal\_eval(r.text), sort\_keys=True,indent=4,separators=(',', ': '))