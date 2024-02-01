platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor

### Sample Usage

Example query for a specific descriptor: 777900478994849

https://graph.facebook.com/777900478994849?access\_token=555|asdF123

Data returned:

{
  "id": "777900478994849",
  "indicator": {
    "indicator": "http://test1435342443.evilevillabs.com/test.php",
    "type": "URI",
    "id": "841478115929947"
  },
  "owner": {
    "id": "682796275165036",
    "name": "Facebook Site Integrity ThreatExchange"
  },
  "type": "URI",
  "raw\_indicator": "http://test1435342443.evilevillabs.com/test.php",
  "description": "Test Description",
  "tags": {
    "data": \[
      {
        "id": "908180082612873",
        "text": "evilevil"
      },
      {
        "id": "884078131700721",
        "text": "testing"
      }
    \]
  },
  "status": "UNKNOWN"
}