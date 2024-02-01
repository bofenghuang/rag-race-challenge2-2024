platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/resharing

### Limiting re-sharing to select members and their related entities with a need to know, using the API

POST https://graph.facebook.com/v2.8/threat\_indicators?access\_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat\_type=MALICIOUS\_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=HAS\_WHITELIST
&amp;privacy\_members=555
&amp;share\_level=AMBER