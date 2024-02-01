platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags

### Sample Usage

Example of tagged objects for a specific ThreatTag: 908180082612873

https://graph.facebook.com/v2.7/908180082612873/tagged\_objects/?access\_token=555|aSdF123GhK

Data returned:

{
  "data": \[
    {
      "id": "1039423046092869",
      "type": "THREAT\_DESCRIPTOR",
      "name": "test1464195852.evilevillabs.com"
    },
    ...
  \]
}

Example of tagged objects for a ThreatTag with the text 'ducks'

https://graph.facebook.com/v2.7/threat\_tags/?access\_token=555|aSdF123GhK&amp;text=ducks&amp;fields=id,text,tagged\_objects

Data returned:

{
  "data": \[
    {
      "id": "501159930008561",
      "text": "ducks"
      "tagged\_objects": {
        "data": \[
          {
            "id": "1162586023812794",
            "type": "THREAT\_DESCRIPTOR",
            "name": "test1469481750.evilevillabs.com"
          },
          ...
        \]
      },
    }
  \]
}