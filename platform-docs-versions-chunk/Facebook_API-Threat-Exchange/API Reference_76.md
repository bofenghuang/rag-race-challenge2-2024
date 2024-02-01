platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/resharing

### Allowing re-sharing to anyone, including public channels, using the API

POST https://graph.facebook.com/v2.8/threat\_indicators?access\_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat\_type=MALICIOUS\_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=VISIBLE
&amp;share\_level=WHITE

### Limiting re-sharing to established, non-public channels, using the API

POST https://graph.facebook.com/v2.8/threat\_indicators?access\_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat\_type=MALICIOUS\_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=VISIBLE
&amp;share\_level=GREEN