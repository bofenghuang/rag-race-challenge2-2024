platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-members


## Parameters

The following query parameter is required:

* **`access_token`** - The key for authenticating to the API. It is a concatenation of <your-app-id>|<your-app-secret>. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
    
* `fields` - A list of fields to return in the response
    

Example query:

https://graph.facebook.com/v2.8/threat\_exchange\_members?access\_token=555|aSdF123GhK

Data returned:

{
  "data": \[
    {
      "id": "820763734618599",
      "email": "threatexchange@support.facebook.com",
      "name": "Facebook ThreatExchange"
    },
    ...
  \]
}

The same query using cURL:

curl -i -X GET \\
 "https://graph.facebook.com/v2.8/threat\_exchange\_members?access\_token=555%7C1234"

The same query using Python:

import requests
import json
import ast
import urllib

app\_id = '555' # Replace this with your app ID
app\_secret = '1234' # Replace this with your app secret

query\_params = urllib.urlencode({
    'access\_token' : app\_id + '|' + app\_secret,
    })

r = requests.get('https://graph.facebook.com/v2.8/threat\_exchange\_members?' + query\_params)

print json.dumps(ast.literal\_eval(r.text), sort\_keys=True,indent=4,separators=(',', ': '))