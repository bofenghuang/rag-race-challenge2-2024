platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator


### Sample Usage

Example query for descriptors related to a specific indicator: 852121234856016

https://graph.facebook.com/`v19.0`/852121234856016/descriptors/?access\_token=555|aSdF123GhK

Data returned:

 {
   "data": \[
  {
    "id": "811927545529339",
    "indicator": {
      "indicator": "test1434227164.evilevillabs.com",
      "type": "DOMAIN",
      "id": "852121234856016"
    },
    "owner": {
      "id": "588498724619612",
      "name": "Facebook CERT ThreatExchange"
    },
    "type": "DOMAIN",
    "raw\_indicator": "test1434227164.evilevillabs.com",
    "description": "This is our test domain. It's harmless",
    "status": "NON\_MALICIOUS"
  },
  {
    "id": "799906626794304",
    "indicator": {
      "indicator": "test1434227164.evilevillabs.com",
      "type": "DOMAIN",
      "id": "852121234856016"
    },
    "owner": {
      "id": "682796275165036",
      "name": "Facebook Site Integrity ThreatExchange"
    },
    "type": "DOMAIN",
    "raw\_indicator": "test1434227164.evilevillabs.com",
    "description": "Malware command and control",
    "status": "MALICIOUS"
  }
\],
"paging": {
  "cursors": {
    "before": "ODExOTI3NTQ1NTI5MzM5",
    "after": "Nzk5OTA2NjI2Nzk0MzA0"
  }
}