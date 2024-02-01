platform: Facebook
topic: Graph-API
subtopic: Whats app business hsm Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business hsm Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | ID  |
| `category`<br><br>enum | The category type of the message template<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `components`<br><br>[list<WhatsAppBusinessHSMWhatsAppHSMComponentGet>](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm-whats-app-hsm-component-get/) | An array of JSON objects describing the message template components.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `cta_url_link_tracking_opted_out`<br><br>bool | Optional boolean field for opting out/in of link tracking at template level |
| `language`<br><br>string | The language (and locale) of the element translation<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `message_send_ttl_seconds`<br><br>integer | Template message delivery retry time-to-live (TTL) override value. If unable to deliver the template message to the WhatsApp user, we will periodically retry for this period of time. If we are unable to deliver the message for this period of time, the message will be dropped.  <br>  <br>Only allowed for authentication message templates. See [Time-To-Live](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates/#time-to-live).<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `name`<br><br>string | The message template name<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `previous_category`<br><br>enum | Previous category of the template. See [Template Categories](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates#categories).<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `quality_score`<br><br>[WhatsAppBusinessHSMWhatsAppBusinessHSMQualityScoreShape](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm-whats-app-business-hsm-quality-score-shape/) | Quality score of the HSM |
| `rejected_reason`<br><br>enum | The reason the message template was rejected<br><br>enum {ABUSIVE\_CONTENT, INVALID\_FORMAT, NONE, PROMOTIONAL, TAG\_CONTENT\_MISMATCH, SCAM} |
| `status`<br><br>enum | The status of the message template<br><br>enum {APPROVED, IN\_APPEAL, PENDING, REJECTED, PENDING\_DELETION, DELETED, DISABLED, PAUSED, LIMIT\_EXCEEDED}<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `sub_category`<br><br>enum | Sub category of the template<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |