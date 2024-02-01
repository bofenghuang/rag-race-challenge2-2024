platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags

## Connections

| Name | Description | Type |
| --- | --- | --- |
| `tagged_objects` | The objects tagged with this text. | `Malware`, `ThreatDescriptor`, `MalwareFamily` |

#### Parameters

The following query parameters are available:

* `tagged_since` - Fetches all objects that have been tagged since this time (inclusive).
    
* `tagged_until` - Fetches all objects that have been tagged until this time (inclusive).
    

Tagged objects are returned in the order based on when the tag was applied, ascending. This timestamp is currently not exposed by the API, but is the same one used by `tagged_since` and `tagged_until`. While this API can be used to create a copy of data in ThreatExchange, the [threat\_updates](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates/v10.0) API may be better suited for your usecase.