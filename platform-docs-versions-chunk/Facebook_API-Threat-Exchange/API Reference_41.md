platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates

### Updating the Table

In order to build your copy of the database, begin polling at `start_time=0`.

For each entry seen:

* Update: `UPSERT INTO MyTableForPrivacyGroup VALUES ($response[id], $response[type], $response)`
* Delete: `DELETE FROM MyTableForPrivacyGroup WHERE indicator_id = $response[id]`

When you completely exhaust `/threat_updates`, you should have a complete and up-to-date copy of the data stored in ThreatExchange.

Store the largest `update_time` that you have seen to use as a the `start_time` for the next time you fetch, as described above.