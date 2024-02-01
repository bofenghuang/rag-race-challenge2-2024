platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/best-practices

### Tailing /threat\_updates API

**Recommended**—[The /threat\_updates](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates) API allows you to exactly reproduce a [ThreatPrivacyGroup](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group/)'s contents. It also allows you to get deletion events as long as you poll within 30 days of the object being deleted. Tailing /threat\_updates gives you the lowest latency, complete data, and is the only API that notifies of deletes.

Not all PrivacyGroups have this API enabled, reach out to threatexchange@meta.com for questions about enabling it.