platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates

## Maintaining a copy of data in a PrivacyGroup using `threat_updates`

The object emitted by `threat_updates` is [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/), and has the same fields and connections. However, the connections are modified such that only data in the given PrivacyGroup are returned.

This allows you to use `/threat_updates` as an update stream to keep a copy of the data, keyed by the `id` of the [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/). The simplest way to do this is use the `fields=` parameter to fetch all the data you are interested in connected data, and store the resultant data.