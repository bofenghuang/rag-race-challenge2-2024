platform: Facebook
topic: API-Threat-Exchange
subtopic: API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Overview.md
url: https://developers.facebook.com/docs/threat-exchange/best-practices

### /<TAG\_ID>/tagged\_objects API

The [/<TAG\_ID>/tagged\_objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags) API allows you to reliably download all ThreatDescriptors tagged with those tags. Because most data is tagged, this is a reliable way to get data. However, you must do client-side filtering to remove unwanted data, but with the same tags (for example, in the wrong privacy group, wrong type, etc). Additionally, because you don't learn of deletions or updates, you must start over from `tagged_since=0` at some interval (for example, 30 days) in order get updates and discard data that has been deleted.