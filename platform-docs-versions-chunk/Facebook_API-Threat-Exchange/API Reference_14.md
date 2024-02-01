platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group

# ThreatPrivacyGroup

A list of [ThreatExchangeMembers](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) to which data can be shared. Only available in versions 2.4+ of the Graph API.

## Fields

| Parameter | Description | Type |
| --- | --- | --- |
| `id` | Unique identifier of the threat privacy group | `number` |
| `name` | The name of the threat privacy group | `string` |
| `description` | A human readable description of the group | `string` |
| `members_can_see` | If true, group members can view this group, including its name, description, and list of members | `boolean` |
| `members_can_use` | If true, members are allowed to use this group to protect their own threat data | `boolean` |

### Sample Usage

To create a privacy group, one could POST to:

https://graph.facebook.com/v2.4/threat\_privacy\_groups?name=GROUP1&amp;description=MYFIRSTGROUP&amp;access\_token=555|asdF123

Data returned:

{
  "id": "123456789101112"
}