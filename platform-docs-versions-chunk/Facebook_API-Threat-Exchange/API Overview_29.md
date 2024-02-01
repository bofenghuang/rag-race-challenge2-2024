platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/ui


## ThreatExchange UI Use Cases

* People at various organizations want to share information about **threats**: malicious URLs, harmful content hashes, malware signatures, and so on.
    
* A [**threat indicator**](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) is the **objective part**: a file hash, a URL, and so on, with a type (MD5, SHA1, URL, and so on).
    
* A [**threat descriptor**](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor) contains an indicator and the **subjective parts**: how malicious a team thinks it is, when they first saw it, and so on.
    
* Meta privacy revolves around **user IDs,** ThreatExchange revolves around **app IDs**. For example, app ID 1064060413755420 is Media Hash Sharing Test. These are generally of the form _Team T at company C_.
    
* When people share threat data, they can specify who they want to see each datum. This is referred to as a **visibility** or **privacy type**.
    
    * _Visible/public_ means all ThreatExchange members can see it.
        
    * Or, for each datum the members can create an app-whitelist of specific teams at specific companies.
        
    * Or, for each datum the members can specify a privacy-group that is simply a predefined list of app IDs.
        
    
* People can [**tag**](https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags) their descriptors. These are tags in any other tool, except that ThreatExchange tags have their own metadata, including the subjective parts that descriptors have, and they also have their own visiblity (public/app-whitelist/privacy-group).
    
* There's more about threat descriptors ([review status](https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type) and [others](https://developers.facebook.com/docs/threat-exchange/reference/apis)) and other types of data shareable on ThreatExchange. For the purpose of this walkthrough, we're focused on indicators, descriptors, visibility, and tags.