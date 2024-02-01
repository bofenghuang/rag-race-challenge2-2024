platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/api-structure


## Queries For Multiple Objects

Queries into ThreatExchange are HTTP GET requests to one of the following URLs:

* [/threat\_descriptors](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptors)
    
* [/threat\_indicators](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicators)
    
* [/threat\_exchange\_members](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-members)
    
* [/threat\_privacy\_groups](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-groups)
    
* [/{privacy\_group\_id}/threat\_updates](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates)
    

**All Graph API objects work in a similar way. After you have [authenticated](https://developers.facebook.com/docs/threat-exchange/getting-started), try some calls with the [`threat_indicator`](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) object.**

To ensure consistency, the ThreatExchange APIs and its consumers use JSON objects as their default currency. Using these APIs gives you a lot of things for free:

* Field validation
    
* Type checking
    
* Persistence to Facebook's Graph
    
* Everyone else can use what you share and be better protected!
    

All objects are formatted as maps using a predefined set of field names, with expected value types. They can be of arbitrary size and field order in the map is, generally, not important.