platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates


## Delete Event TTL, Polling Frequency, and Checkpointing

Deletion events **are only stored for 90 days**, and so you must poll more frequently than that, or your copy of the database will become invalid. We generally recommend polling daily to prevent a large backlog of updates from accruing, and many platforms will want to poll more frequently than that to have a lower latency between sharing and ingestion. We don't recommend polling more frequently than 1/minute.

To resume from where you last left off, set the `start_time` to the largest `update_time` you have previously seen. It is important that you not attempt to use the time you completed your last fetch as the checkpoint, as there may be a small delay between when updates are written and when they appear in `/threat_updates`.

`start_time` is inclusive, so you may see updates you have already seen when there is not much activity in a PrivacyGroup.

This call may reveal indicators that have been removed from the privacy group. When you recieve notice of a deletion, you should remove it from your copy of ThreatExchange data, as it may have been previously shared in error. See [Terms and Conditions](https://www.facebook.com/legal/threatexchange_terms) for more.