platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/deleting

# Delete Data

ThreatExchange currently supports deletion for [ThreatDescriptor](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptors) objects and relationships between [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) objects. Some objects may also be given an expiration time, which will cause data to be deleted automatically within 90 days of the expiration.

You can delete a ThreatDescriptor using the API with a `DELETE HTTP` request:

DELETE https://graph.facebook.com/v2.11/<object\_id>

After a subjective ThreatDescriptor is deleted, the objective ThreatIndicator may still exist.

To delete a relationship between ThreatIndicators using the API:

DELETE https://graph.facebook.com/v2.11/<object\_id>/related?related\_id=<object\_id\_2>

We do not support deletes for Tags.