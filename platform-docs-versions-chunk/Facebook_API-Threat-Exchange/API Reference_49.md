platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptors

# /threat\_descriptors

NOTE: Queries using this call are not guaranteed to be comprehensive and may only return partial results. See how to do bulk download in [Best Practices](https://developers.facebook.com/docs/threat-exchange/best-practices).

The API call enables searching for subjective opinions on indicators stored in ThreatExchange. With this call you can search by free text, type, submitter, or all in a specific time window. Combinations of these query types are also allowed. This call is only permitted on Platform versions 2.4 and later.  
  
This query may only return partial results and should only be used to find examples of ThreatDescriptors matching the query parameters. To get a comprehensive list of ThreatDescriptors you should use the [`\threat_tags` endpoint](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-tags) and do any necessary post-process filtering