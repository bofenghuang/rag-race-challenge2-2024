platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/api

## Publishing Data Using the API

**Test publish** a domain, `my-test-example.com`, ensuring only you are able to see the data:

https://graph.facebook.com/threat\_descriptors

POST DATA

type=DOMAIN
indicator=my-test-example.com
privacy\_type=HAS\_WHITELIST
status=UNKNOWN
description=Test data publishing
share\_level=RED
privacy\_members=<your\_app\_id>
access\_token=555|1235

The return value will be a JSON map with a success or failure code and, if the call is successful, the unique ThreatExchange ID for the descriptor you published!

**Publish** a descriptor for your own domain, `my-company-domain.com`, and share it with Facebook's app ID, `820763734618599`:

https://graph.facebook.com/threat\_descriptors

POST DATA

type=DOMAIN
indicator=my-company-domain.com
privacy\_type=HAS\_WHITELIST
status=NON\_MALICIOUS
description=The domain owned by <your\_app\_id>
share\_level=WHITE
privacy\_members=820763734618599
access\_token=555|1235