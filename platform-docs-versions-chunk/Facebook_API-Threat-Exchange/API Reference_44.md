platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates


## Parameters

The following query parameters are available (bold parameters are required):

* **`access_token`** - The key for authenticating to the API.
    
* `types` - The types of indicators to search for.
    
* `start_time` - Search for indicators that last updated on or after this timestamp.
    
* `stop_time` - Search for indicators that last updated before this timestamp.
    
* `limit` - Defines the maximum size of a page of results
    
* `fields` - A list of fields to return in the response, if not specified all fields are returned.
    
    * `id` - The id of the ThreatIndicator
        
    * `should_delete` - Whether this is an update or deletion event
        
    * `last_updated` - The checkpointable timestamp of the update.
        
    * `type` - Unchanged from [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/)
        
    * `indicator` \- Unchanged from [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/)
        
    * `descriptors` - A list of [ThreatDescriptor objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor/) in this PrivacyGroup.
        
        * Clients that want to deeply inspect data should refer to the fields selection in [ThreatDescriptor objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor/) - you can nest field selections with curly braces: example: `fields=descriptors{owner{name}}`
            
        
    * `tags` A shortcut for a flattened list of tag names from `descriptors{tags{name}}`
        
    * `status` A shortcut to taking the highest severity status from`descriptors{status, reactions}`
        
    * `applications_with_opinions` A shortcut for a flattened list of ThreatExchange member ids from `descriptors{owner, reactions{owner}}`
        
    

Example query for all indicators that last updated between December 2019 (1575187200) to March 2020 (1583049600) for privacy group 123456789012345:

https://graph.facebook.com/`v19.0`/123456789012345/threat\_updates/?access\_token=555|aSdF123GhK&start\_time=1575187200&stop\_time=1583049600&fields=id,indicator,type,creation\_time,last\_updated,should\_delete,tags,status,applications\_with\_opinions

Data Returned:

{
    "data": \[
        {
            'id': '123456',
            'indicator': 'a\_hash\_that\_was\_created\_or\_updated',
            'type': 'HASH\_PDQ',
            'creation\_time': 1581977111,
            'last\_updated': 1582372222,
            'should\_delete': False,
            'tags': \['tag1', 'another\_tag'\],
            'status': 'MALICIOUS',
            'applications\_with\_opinions': \['1234567890'\]
        },
				{
            'id': '123457',
            'indicator': 'a\_hash\_that\_should\_be\_deleted',
            'type': 'HASH\_PDQ',
            'creation\_time': 1581977111,
            'last\_updated': 1582372222,
            'should\_delete': True,
            'tags': \['tag1', 'another\_tag'\],
            'status': 'MALICIOUS',
            'applications\_with\_opinions': \['1234567890'\]
        },
        ...
    \]
    "paging": {
        "cursors": {
            "before": "MjVFR",
            "after": "MjQZD"
        }
    "next": "https://graph.facebook.com/`v19.0`/123456789012345/threat\_updates/?access\_token=555|aSdF123GhK&start\_time=1575187200&stop\_time=1583049600&types=HASH\_MD5,HASH\_PDQ&fields=id,indicator,type,creation\_time,last\_updated,should\_delete,tags,status,applications\_with\_opinions&after=MjQZD"
    }