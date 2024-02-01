platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/message_templates/

### Parameters

| Parameter | Description |
| --- | --- |
| `category`<br><br>array<enum {ACCOUNT\_UPDATE, PAYMENT\_UPDATE, PERSONAL\_FINANCE\_UPDATE, SHIPPING\_UPDATE, RESERVATION\_UPDATE, ISSUE\_RESOLUTION, APPOINTMENT\_UPDATE, TRANSPORTATION\_UPDATE, TICKET\_UPDATE, ALERT\_UPDATE, AUTO\_REPLY, TRANSACTIONAL, OTP, UTILITY, MARKETING, AUTHENTICATION}> | The category for a template |
| `content`<br><br>string | The content for a template |
| `language`<br><br>array<string> | A list of supported languages that are available for each template |
| `name`<br><br>string | The name for a message template |
| `name_or_content`<br><br>string | Returns a list of message templates where the value for `name` or `content` match this value |
| `quality_score`<br><br>array<enum {GREEN, YELLOW, RED, UNKNOWN}> | The quality score for a template |
| `status`<br><br>array<enum {APPROVED, IN\_APPEAL, PENDING, REJECTED, PENDING\_DELETION, DELETED, DISABLED, PAUSED, LIMIT\_EXCEEDED}> | The review status for a template |