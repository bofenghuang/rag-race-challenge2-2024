platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/best-practices


## Include Nested Fields and Objects in Result Data

It can sometimes be more efficient to include various nested fields or related objects in your search results. The following syntax shows how, for the `facebook.com` indicator object, to pull all of its descriptors without issuing additional API calls:

https://graph.facebook.com/v2.8/788497497903212?fields=descriptors{owner,description,status,share\_level},indicator,type&amp;access\_token=<access\_token>

RESULT:
{
  "descriptors": {
    "data": \[
      {
        "owner": {
          "id": "820763734618599",
          "name": "Facebook Administrator"
        },
        "description": "Facebook",
        "status": "NON\_MALICIOUS",
        "share\_level": "GREEN",
        "id": "834469179976904"
      },
      {
        "owner": {
          "id": "588498724619612",
          "name": "Facebook CERT ThreatExchange"
        },
        "description": "Non malicious",
        "status": "NON\_MALICIOUS",
        "share\_level": "GREEN",
        "id": "1202389109786630"
      }
    \],
    "paging": {
      "cursors": {
        "before": "ODM0NDY5MTc5OTc2OTA0",
        "after": "MTIwMjM4OTEwOTc4NjYzMAZDZD"
      }
    }
  },
  "indicator": "facebook.com",
  "type": "DOMAIN",
  "id": "788497497903212"
}