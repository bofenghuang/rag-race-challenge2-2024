platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates

# /<privacy-group>/threat\_updates

This call is not currently enabled for all PrivacyGroups. A 500 error will be returned if this call is used with PrivacyGroup that doesn't have \`/threat\_updates\` enabled. If you would like to enable this call for your PrivacyGroup please [contact the ThreatExchange team](mailto:threatexchange@fb.com).

ThreatExchange provides [multiple APIs](https://developers.facebook.com/docs/threat-exchange/reference/apis/) for querying data. Most of these APIs will only allow you to know the current state of the object, and if it is later updated or removed, you can only learn of changes by polling the objects again. ThreatExchange API integration works best when you can keep an up-to-date copy of the information that you are interested in, and re-polling all data would be cumbersome.

`/threat_updates` provides a solution to keeping a copy of data within a PrivacyGroup, specifically for the data that users tell us they most need kept up to date. `/threat_updates` allows for a specific projection of the ThreatExchange graph database to turn it into a list of signals with opinions. By tailing `/threat_updates`, you can learn of updates to that projection within seconds, and so the liveness of the data is only limited by how frequently you poll.

When data in the PrivacyGroup is updated, an event is moved to the "end" of the update list. All updates are ordered by `update_time`, and you can save this time to resume fetching from where you left off.