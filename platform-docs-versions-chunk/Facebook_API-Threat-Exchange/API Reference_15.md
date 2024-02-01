platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group

## Connections

| Name | Description | Type |
| --- | --- | --- |
| `members` | Members of the privacy group | [`ThreatExchangeMember`](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) |

### Sample Usage

Example query for a specific privacy group: 123456789101112

https://graph.facebook.com/v2.4/123456789101112/members/?access\_token=555|aSdF123GhK

Data returned:

{
  "data": \[
    {
      "id": "999999999999",
      "email": "threatexchange@domain.com",
      "name": "Facebook Administrator"
    }
    ...
  \]
}