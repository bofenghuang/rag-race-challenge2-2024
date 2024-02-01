platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/api

## Searching Data Using the API

With your newly activated access token, perform a search for malicious URLs added in the last week:

https://graph.facebook.com/threat\_descriptors?type=URI&amp;status=MALICIOUS&amp;since=a week ago&amp;access\_token=<access\_token>

Please note that not all fields are returned by default. Consult the reference documentation and specify the fields you are looking to read by appending the fields parameter. See the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#reading) for more details.