platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/submitting

## Uploading using the API

You may submit data using the ThreatExchange API via an HTTP POST to the following URL:

* https://graph.facebook.com/v4.0/threat\_descriptors
    

NOTE: The call to /threat\_indicators is deprecated as of v2.4 of the ThreatExchange API. If you attempt to access this endpoint in v2.4+, it will create a threat descriptor and the associated threat indicator behind the scenes.

Example submission of a malicious domain using the API:

https://graph.facebook.com/v4.0/threat\_descriptors?access\_token=555|aSdF123GhK

POST DATA:
indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;tags=testingtags
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=VISIBLE

Data returned:

{
"id": "853037291373757",
"success": true
}