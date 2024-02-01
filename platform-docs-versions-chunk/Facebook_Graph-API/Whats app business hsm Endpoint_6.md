platform: Facebook
topic: Graph-API
subtopic: Whats app business hsm Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business hsm Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm/


### Parameters

| Parameter | Description |
| --- | --- |
| `allow_category_change`<br><br>boolean | Set to `true` to allow us to assign a category based on our [template guidelines](https://developers.facebook.com/docs/whatsapp/updates-to-pricing/new-template-guidelines) and the template's contents. This can prevent the template `status` from immediately being set to `REJECTED` upon creation due to miscategorization.<br><br>  <br>If omitted, template will not be auto-assigned a category and its status may be set to `REJECTED` if determined to be miscategorized.<br><br>  <br>See [Template Categories](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/#categories). |
| `category`<br><br>enum {UTILITY, MARKETING, AUTHENTICATION} | Template category. See [Template Categories](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/#categories).<br><br>Required |
| `components`<br><br>array<JSON object> | Array of components that make up the template. See [Template Components](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/components).<br><br>  <br>For types `HEADER`, `BODY`, `FOOTER`, `text` is required.<br><br>Required |
| `type`<br><br>enum {HEADER, BODY, FOOTER, BUTTONS, CAROUSEL, LIMITED\_TIME\_OFFER} | Component type.<br><br>Required |
| `format`<br><br>enum {TEXT, IMAGE, DOCUMENT, VIDEO, LOCATION} | Component format. |
| `text`<br><br>string | **Required for components with type `HEADER`,`BODY`, or `FOOTER`.**<br><br>  <br>Component text. |
| `buttons`<br><br>array<JSON object> | Button components to be used in the template. |
| `type`<br><br>enum {QUICK\_REPLY, URL, PHONE\_NUMBER, OTP, MPM, CATALOG, VOICE\_CALL} | Button type.<br><br>Required |
| `text`<br><br>string | Button text. |
| `url`<br><br>URI | url |
| `phone_number`<br><br>phone number string | phone\_number |
| `example`<br><br>array<string> | example |
| `flow_id`<br><br>int64 | flow\_id |
| `zero_tap_terms_accepted`<br><br>boolean | zero\_tap\_terms\_accepted |
| `example`<br><br>JSON object | Placeholder examples. Templates will not be approved without examples. |
| `header_text`<br><br>array<string> | header\_text |
| `body_text`<br><br>array<array<string>> | body\_text |
| `header_handle`<br><br>array<string> | header\_handle |
| `language`<br><br>string | Template [location and locale code](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/supported-languages).<br><br>Required |
| `name`<br><br>string | Template name.<br><br>Required |
| `sub_category`<br><br>enum {CUSTOM, ORDER\_DETAILS, ORDER\_STATUS} | Sub category of the template |