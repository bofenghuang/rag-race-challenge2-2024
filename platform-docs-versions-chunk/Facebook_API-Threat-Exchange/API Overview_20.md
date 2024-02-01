platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/best-practices

# Best Practices for Using ThreatExchange

This guide explains some ways to use ThreatExchange that will help improve throughput and usage.

## Downloading Data

When you get access to new data in ThreatExchange (such as by being added to a PrivacyGroup), we recommend you get a sample or complete copy of the data to evaluate it.

You can use these APIs and UI:

* [ThreatExchange UI](#sample-csvs) - sample data
* [/threat\_descriptors API](#threat-descriptors-api) - samples data
* [/threat\_updates API](#threat-updates-api) - Recommended API for complete copy
* [/<TAG\_ID>/tagged\_objects API](#tagged-objects-api) - Okay for a 1-time complete copy

Only some of them should be used for automated integration into your own systems, and the others should be used only for sampled evaluation and testing.