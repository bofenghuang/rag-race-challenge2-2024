platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/api


## More API Examples

**Search** for all compromised credentials found on the Internet within the last day:

https://graph.facebook.com/`v19.0`/threat\_indicators?type=COMPROMISED\_CREDENTIAL&since=yesterday&access\_token=555|1235\]
        

**Find** the unique ThreatExchange ID for a specific indicator, such as `facebook.com`:

https://graph.facebook.com/`v19.0`/threat\_indicators?text=facebook.com&access\_token=555|1235
        

**Explore** related indicators for a specific indicator with ThreatExchange ID `898557073557972`:

https://graph.facebook.com/898557073557972/descriptors?access\_token=555|1235

**Explore** all of the descriptors for a specific indicator with ThreatExchange ID `898557073557972`:

https://graph.facebook.com/898557073557972/descriptors?access\_token=555|1235

See more examples on our [Github](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange&h=AT1aeVDOOM6CGWw0H3V5o60NaX1CM12xQYiZgY1uw4fLMgJAywudPRrx_w3PhOe49ZMI97sb4J1WcFZA8pAW0TsCU4yrJXbd8-txpNksHDpPYMUghxbeo_2H-Thfq7Gzt8uW4gGZiZjjbszQ), or on the endpoint pages for [threat indicators](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicators), [threat descriptors](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptors).