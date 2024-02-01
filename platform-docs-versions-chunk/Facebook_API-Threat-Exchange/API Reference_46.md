platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-tags


## Parameters

The following query parameters are available (bold parameters are required):

* **`access_token`** - The key for authenticating to the API.
    
* **`text`** - Freeform text field with a value to search for. This value should describe a broader type or class of attack you are interested in.
    
* `fields` - A list of fields to return in the response
    
* `subscribed` - when POSTing to a specific tag, will subscribe you to a tag for Webhooks
    

Example query for all tags which start with `malware`:

https://graph.facebook.com/`v19.0`/threat\_tags?access\_token=555|aSdF123GhK&text=malware

{
  "data": \[
    {
      "id": "1318516441499594",
      "text": "malware"
    },
    {
      "id": "1104531542952223",
      "text": "malwaresite"
    },
    ...
}

The same query using a cURL:

curl -i -X GET \\
 "https://graph.facebook.com/v14.0/threat\_tags?access\_token=555|7C1234&amp;text=malware"

The same query in Python:

import requests
import json
import ast
import urllib

app\_id = '555' # Replace this with your app ID
app\_secret = '1234' # Replace this with your app secret
text = 'malware'

query\_params = urllib.urlencode({
    'access\_token' : app\_id + '|' + app\_secret,
    'text' : text
    })

r = requests.get('https://graph.facebook.com/v14.0/threat\_tags?' + query\_params)

print json.dumps(ast.literal\_eval(r.text), sort\_keys=True,indent=4,separators=(',', ': '))

Example query for tags which start with `ducks` and fetching the tagged objects.

https://graph.facebook.com/`v19.0`/threat\_tags/?access\_token=555|aSdF123GhK&text=ducks&fields=id,text,tagged\_objects

Data returned:

{
  "data": \[
    {
      "id": "501159930008561",
      "text": "ducks"
      "tagged\_objects": {
        "data": \[
          {
            "id": "1162586023812794",
            "type": "THREAT\_DESCRIPTOR",
            "name": "test1469481750.evilevillabs.com"
          },
          ...
        \]
      },
    }
  \]
}