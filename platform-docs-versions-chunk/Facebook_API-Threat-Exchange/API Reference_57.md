platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/app-id-threat-privacy-groups-member

# /<app-id>/threat\_privacy\_groups\_member

Returns a list of the [ThreatPrivacyGroups](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group/) of which your app is a member.

## Parameters

The following query parameter is required:

* **`access_token`** - The key for authenticating to the API. It is a concatenation of <your-app-id>|<your-app-secret>. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
    

The following query parameters are optional:

* `name` - Allows filtering by privacy group name
    
* `description` - Allows filtering by privacy group description
    

Example query:

https://graph.facebook.com/v2.4/<your-app-id>/threat\_privacy\_groups\_member?access\_token=555|aSdF123GhK

Data returned:

{
  "data": \[
    {
      "name": "MYNAMEISBOB",
      "description": "MALWARESIGNATURES",
      "group\_id": "7777777777"
    },
    ...
  \]
}