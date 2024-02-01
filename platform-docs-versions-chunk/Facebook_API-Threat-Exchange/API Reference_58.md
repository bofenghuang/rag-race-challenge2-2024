platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/privacy

# ThreatExchange Privacy Controls

All submissions to the ThreatExchange API allow for limiting the visibility of any [ThreatDescriptor](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor) objects. Currently, ThreatExchange supports three levels of visibility:

* allow all members;
    
* allow a [ThreatPrivacyGroup](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group/); and
    
* allow a whitelist of specific members.
    

The desired privacy setting on an object is specified by the values at the time of a create or edit submission to the API. Privacy settings can also be changed retroactively for data you've already submitted.

Privacy settings are propagated as follows: Threat Exchange members can see an indicator if and only if they can see at least one associated descriptor.