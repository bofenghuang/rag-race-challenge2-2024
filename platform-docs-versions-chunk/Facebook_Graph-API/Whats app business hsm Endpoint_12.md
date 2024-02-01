platform: Facebook
topic: Graph-API
subtopic: Whats app business hsm Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business hsm Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/compare/

### Limitations

* Only two templates can be compared at a time.
* Templates must have been sent at least 1,000 times in the queries specified timeframe.
* Timeframes are limited to 7, 30, 60 and 90 day lookbacks from the time of the request.

### Request Syntax

GET /<WHATSAPP\_MESSAGE\_TEMPLATE\_ID>/compare
  ?template\_ids=\[<TEMPLATE\_IDS\]
  &start=<START>
  &end=<END>

### Response

{
  "data": \[
    {
      "metric": "BLOCK\_RATE",
      "type": "RELATIVE",
      "order\_by\_relative\_metric": \[<ORDER\_BY\_RELATIVE\_METRIC>\]
    },
    {
      "metric": "MESSAGE\_SENDS",
      "type": "NUMBER\_VALUES",
      "number\_values": \[<NUMBER\_VALUES>\]
    },
    {
      "metric": "TOP\_BLOCK\_REASON",
      "type": "STRING\_VALUES",
      "string\_values": \[<STRING\_VALUES>\]
    }
  \]
}

### Sample Request

curl -X GET 'https://graph.facebook.com/`v19.0`/5289179717853347/compare?template\_ids=\[1533406637136032\]&start=1674844791182&end=1674845395982' \\
-H 'Authorization: Bearer EAAJB...'