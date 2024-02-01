platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/resharing

# ThreatExchange re-sharing controls

All submissions to the ThreatExchange API allow for defining how the data can be re-shared by its recipients. The level of re-sharing is applied via the `share_level` attribute.

The desired re-share setting on an object can be specified at the time of a create or edit submission to the API. While re-sharing settings can be changed retroactively, those changes will not be pushed as updates to members that have already accessed the data.