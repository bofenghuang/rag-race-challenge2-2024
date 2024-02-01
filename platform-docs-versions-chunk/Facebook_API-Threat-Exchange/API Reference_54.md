platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-groups

## Parameters

The following query parameters are available (bold parameters are required):

* **`access_token`** - The key for authenticating to the API. It is a concatenation of \[your-app-id|your-app-secret\]. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
    
* **`name`** - The name of the threat privacy group.
    
* **`description`** - A human readable description of the group.
    
* `members` - A list of [ThreatExchangeMembers](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) to be added to the group. Can be modified later.
    
* `members_can_see` - If true, group members can view this group, including its name, description, and list of members. Defaults to FALSE.
    
* `members_can_use` - If true, members are allowed to use this group to protect their own threat data. Defaults to FALSE.