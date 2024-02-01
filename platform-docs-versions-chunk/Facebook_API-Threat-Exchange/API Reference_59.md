platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/privacy


## Privacy Fields

There are two fields that combine to define the privacy on an object within ThreatExchange: `privacy_type` and `privacy_members`.

The `privacy_type` field can have one of the following values:

| Name | Description |
| --- | --- |
| `HAS_PRIVACY_GROUP` | The privacy group IDs specified in `privacy_members` can see the object, while the rest of the member community cannot. |
| `HAS_WHITELIST` | The App IDs specified in `privacy_members` can see the object, while the rest of the member community cannot. |
| `VISIBLE` | All members of ThreatExchange can see the object. _This is the default, if no value is specified._ |

The `privacy_members` field is a comma-delimited list of App IDs of [ThreatExchangeMembers](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) or [ThreatPrivacyGroups](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group/) that are either given or not given access to the data, based on the value in `privacy_type`.