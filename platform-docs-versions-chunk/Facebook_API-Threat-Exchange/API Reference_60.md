platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/privacy

## Setting Privacy: Examples

The following is an examples are submissions of a new malicious domain to ThreatExchange. In each example, we define which members of ThreatExchange are allowed to see the data.

### Controlling visibility using the UI

### Allowing all members access using the API

POST https://graph.facebook.com/v4.0/threat\_descriptors?access\_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat\_type=MALICIOUS\_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=VISIBLE

### Limiting privacy to a privacy group using the API

POST https://graph.facebook.com/v4.0/threat\_descriptors?access\_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat\_type=MALICIOUS\_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=HAS\_PRIVACY\_GROUP
&amp;privacy\_members=123456789