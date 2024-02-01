platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates

### Example Table Schema

Here's is a sample database table schema you could use (for a single PrivacyGroup):

| Column | Type | Note |
| --- | --- | --- |
| indicator\_id | 64 bit integer (Primary Key) | An opinion connected to the ThreatIndicator has been created or updated. Fetch connected data to get updates. |
| indicator\_type | string | The type of the signal (e.g. HASH\_MD5). Each type usually needs type-specific handling, so you could provide a secondary index on (type, update\_time) to checkpoint your own internal processing. This column is an example of parsing specific data out of the payload for the purposes of indexing - you may find you are interested in other fields as well. |
| json\_payload | JSON | The raw JSON, including connections fetched by `fields=` returned by the API. |