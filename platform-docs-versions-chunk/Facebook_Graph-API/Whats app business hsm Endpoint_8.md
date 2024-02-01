platform: Facebook
topic: Graph-API
subtopic: Whats app business hsm Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business hsm Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/


### Parameters

| Parameter | Description |
| --- | --- |
| `category`<br><br>enum {UTILITY, MARKETING, AUTHENTICATION} | category |
| `components`<br><br>array<JSON object> | The array containing all the content of the message template |
| `type`<br><br>enum {HEADER, BODY, FOOTER, BUTTONS, CAROUSEL, LIMITED\_TIME\_OFFER} | Component type.<br><br>Required |
| `format`<br><br>enum {TEXT, IMAGE, DOCUMENT, VIDEO, LOCATION} | Component format. |
| `text`<br><br>string | **Required for components with type `HEADER`,`BODY`, or `FOOTER`.**<br><br>  <br>Component text. |
| `buttons`<br><br>array<JSON object> | Button components to be used in the template. |
| `type`<br><br>enum {QUICK\_REPLY, URL, PHONE\_NUMBER, OTP, MPM, CATALOG, VOICE\_CALL} | Button type.<br><br>Required |
| `text`<br><br>string | Button text. |
| `url`<br><br>URI | url |
| `phone_number`<br><br>phone number string | phone\_number |
| `flow_id`<br><br>int64 | flow\_id |
| `zero_tap_terms_accepted`<br><br>boolean | zero\_tap\_terms\_accepted |
| `message_send_ttl_seconds`<br><br>int64 | Template message delivery retry time-to-live (TTL) override value. If unable to deliver the template message to the WhatsApp user, we will periodically retry for this period of time. If we are unable to deliver the message for this period of time, the message will be dropped.  <br>  <br>Only allowed for authentication message templates. See [Time-To-Live](https://developers.facebook.com/docs/whatsapp/business-management-api/authentication-templates/#time-to-live). |