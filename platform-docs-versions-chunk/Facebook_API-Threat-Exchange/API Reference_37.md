platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates

## Update Events

`/threat_updates` entries represent one of two events, which can be differentiated using the `should_delete` flag.

| Event | `should_delete` | Meaning |
| --- | --- | --- |
| Update | false | An opinion connected to the ThreatIndicator has been created or updated. Fetch connected data to get updates. |
| Delete | true | A ThreatIndicator has been removed from the PrivacyGroup or deleted. |

Otherwise, entries returned by this API behave as [ThreatIndicator Objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/), with additional fields described below.