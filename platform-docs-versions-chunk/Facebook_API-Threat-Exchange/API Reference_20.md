platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags


## Creating a New Tag

You can create a ThreatTag on-the-fly while creating a ThreatDescriptor. If the ThreatTag does not exist, a new one will be created and applied to the new ThreatDescriptor.

https://graph.facebook.com/v2.7/threat\_descriptors?access\_token=555|aSdF123GhK

POST DATA:
  tags=cows,bar
  &amp;type=DOMAIN
  &amp;indicator=test1466722733.evilevillabs.com
  &amp;description=this is an example with tags
  &amp;privacy\_type=VISIBLE
  &amp;share\_level=GREEN
  &amp;status=UKNOWN

Data returned:

{
  "success": true,
  "id": "1162586023812794"
}

To create a ThreatTag without labeling any objects, you can post to the /threat\_tags endpoint explicitly:

https://graph.facebook.com/v2.7/threat\_tags?access\_token=555|aSdF123GhK

POST DATA:
  text=superlongtagfortestingcreation
  &amp;objects=973966502652751,898684593584287

Data returned:

{
  "success": true,
  "id": "1373232162693002"
}

Example of updating a ThreatDescriptor with more tags. If the tag does not exist, a new one will be created and applied to this ThreatDescriptor.

https://graph.facebook.com/v2.7/1162586023812794?access\_token=555|aSdF123GhK

POST DATA:
  tags=ducks,chicken

Data returned:

{
  "success": true
}