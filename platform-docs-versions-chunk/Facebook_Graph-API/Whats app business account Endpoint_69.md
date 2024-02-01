platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/upsert_message_templates/


### Parameters

| Parameter | Description |
| --- | --- |
| `category`<br><br>enum {AUTHENTICATION} | Template category. See Template Categories.<br><br>Required |
| `components`<br><br>array<JSON object> | Array of components that make up the template. See Template Components.<br><br>Required |
| `type`<br><br>enum {HEADER, BODY, FOOTER, BUTTONS, CAROUSEL, LIMITED\_TIME\_OFFER} | type<br><br>Required |
| `add_security_recommendation`<br><br>boolean | Set to true if you want the template to include the string, For your security, do not share this code. Set to false to exclude the string. |
| `code_expiration_minutes`<br><br>int64 | Indicates number of minutes the password or code is valid.<br><br>If omitted, the code expiration warning will not be displayed in the delivered message.<br><br>Minimum 1, maximum 90. |
| `buttons`<br><br>array<JSON object> | Button components to be used in the template. |
| `type`<br><br>enum {OTP} | type<br><br>Required |
| `otp_type`<br><br>enum {COPY\_CODE, ONE\_TAP, ZERO\_TAP} | Indicates button type. Set to COPY\_CODE if you want the template to use a copy code button, or ONE\_TAP to have it use a one-tap autofill button. |
| `package_name`<br><br>string | One-tap buttons only.<br><br>Your Android app's package name. |
| `signature_hash`<br><br>string | One-tap buttons only.<br><br>Your app signing key hash. |
| `languages`<br><br>array<string> | array of Template location and locale code.<br><br>Required |
| `name`<br><br>string | Template name.<br><br>Required |