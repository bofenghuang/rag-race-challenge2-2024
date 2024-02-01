platform: Facebook
topic: Graph-API
subtopic: Whats app business hsm Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business hsm Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/compare/

### Parameters

| Parameter | Description |
| --- | --- |
| `end`<br><br>datetime/timestamp | UNIX timestamp indicating end of timeframe. Timeframes are limited to 7, 30, 60 and 90 day lookbacks from the time of the request. To define a timeframe, set your end date to the current time as a UNIX timestamp, then subtract the number of days for your desired timeframe, in seconds, from that value:<br><br>Required |
| `start`<br><br>datetime/timestamp | UNIX timestamp indicating start of timeframe. Timeframes are limited to 7, 30, 60 and 90 day lookbacks from the time of the request. To define a timeframe, set your end date to the current time as a UNIX timestamp, then subtract the number of days for your desired timeframe, in seconds, from that value:<br><br>Required |
| `template_ids`<br><br>array<EntWhatsAppBusinessHSM ID> | ID of the WhatsApp Message Template to compare the target to.<br><br>Required |