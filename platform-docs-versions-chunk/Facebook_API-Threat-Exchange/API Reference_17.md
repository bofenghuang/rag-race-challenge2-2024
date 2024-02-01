platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags

### Sample Usage

Example query for a specific ThreatTag: 908180082612873

Data returned:

{
  "id": "908180082612873",
  "text": "evilevil"
}

Example of searching for a tag by text 'evilevil'. Note that partial tag search is supported.

https://graph.facebook.com/v2.7/threat\_tags/?access\_token=555|aSdF123GhK&amp;text=evilevil

Data returned:

{
  "data": \[
    {
      "id": "908180082612873",
      "text": "evilevil"
    }
    ...
  \]
}