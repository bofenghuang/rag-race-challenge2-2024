platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/conversation_analytics/


### Parameters

| Parameter | Description |
| --- | --- |
| `conversation_categories`<br><br>array<enum {UNKNOWN, MARKETING, UTILITY, AUTHENTICATION, SERVICE, MARKETING\_OPTIMIZED\_DELIVERY}> | Default value: `[]`<br><br>list of conversation categories |
| `conversation_directions`<br><br>array<enum {UNKNOWN, BUSINESS\_INITIATED, USER\_INITIATED}> | Default value: `[]`<br><br>list of conversation directions |
| `conversation_types`<br><br>array<enum {UNKNOWN, REGULAR, FREE\_ENTRY\_POINT, FREE\_TIER}> | Default value: `[]`<br><br>list of conversation types |
| `country_codes`<br><br>array<string> | Default value: `[]`<br><br>list of country codes |
| `dimensions`<br><br>array<enum {UNKNOWN, PHONE, COUNTRY, CONVERSATION\_TYPE, CONVERSATION\_DIRECTION, CONVERSATION\_CATEGORY}> | Default value: `[]`<br><br>list of breakdown dimensions |
| `end`<br><br>int64 | end time<br><br>Required |
| `granularity`<br><br>enum {HALF\_HOUR, DAILY, MONTHLY} | data granularity<br><br>Required |
| `metric_types`<br><br>array<enum {UNKNOWN, CONVERSATION, COST}> | Default value: `[]`<br><br>list of metric types |
| `phone_numbers`<br><br>array<string> | Default value: `[]`<br><br>list of phone numbers |
| `start`<br><br>int64 | start time<br><br>Required |