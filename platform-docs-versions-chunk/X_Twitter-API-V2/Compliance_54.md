platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/streams/api-reference/get-tweets-compliance-stream

### Example responses

* [Successful response](#tab0)

Successful response

      `{   "data": {     "delete": {       "tweet": {         "id": "1542870758724145153",         "author_id": "906948460078698496"       },       "event_at": "2022-07-01T21:48:43.030Z"     }   } }`
    

### Response fields

| Name | Type | Description |
| --- | --- | --- |
| `delete` | string | A delete Tweet event. |
| `withheld` | string | A withheld Tweet event. |
| `drop` | string | A drop Tweet event. |
| `undrop` | string | A undrop Tweet event. |
| `id` | string | The ID of the Tweet triggering a compliance event. |
| `author_id` | string | The ID of the author of a Tweet triggering a compliance event. |
| `event_at` | date (ISO 8601) | Time of when event happended. |