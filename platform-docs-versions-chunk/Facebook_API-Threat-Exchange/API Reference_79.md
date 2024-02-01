platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/reacting


## Values

As of Jan 2023:

| Name | Usage Category | Description |
| --- | --- | --- |
| `SAW_THIS_TOO` | Ingestion status. | The object has been observed on-platform by the reactor. Using this reaction can help track platform spread. |
| `NON_MALICIOUS` | Feedback after review. | The object has been reviewed and found to be non-malicious. This is equivalent to uploading the same object but with the [`StatusType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/status-type) of `NON_MALICIOUS`. A reaction is often preferable, as it will not leave extra objects in ThreatExchange if the original object is later retracted. |
| `DISAGREE_WITH_TAGS` | Feedback after review. | The object has been reviewed and the reactor would have tagged it differently. Many PrivacyGroups use tags in order to categorize data by convention. `DISAGREE_WITH_TAGS` without an upload by the same reactor with their preference in tagging is equivalent to a `NON_MALICIOUS` report. If the owner of the object changes the tags, this reaction will automatically be removed. |
| `HELPFUL` | Ad-hoc feedback. | The object helped lead to the discovery of harmful content. |
| `NOT_HELPFUL` | Ad-hoc feedback. | The object seems to lead to non-malicious content. |
| `OUTDATED` | Ad-hoc feedback. | The object is outdated or can no longer be evaluated. |
| `WANT_MORE_INFO` | Request for information. | More information requested about this object. |
| `INGESTED` | Ingestion status. | The object is outdated or can no longer be evaluated. |
| `ALREADY_KNOWN` | Ingestion status. | The object is equivalent to information already known to the reactor. |
| `IN_REVIEW` | Ingestion status. | The object is being reviewed, or the object has been matched to content on platform that is being reviewed. |
| `REVIEWED` | Ingestion status. | The object has been reviewed, or the object has been matched to content on platform thathas been reviewed. |