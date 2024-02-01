platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | ID of the WhatApp Business Account.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `account_review_status`<br><br>enum | Status from account review process. |
| `analytics`<br><br>[WABAAnalytics](https://developers.facebook.com/docs/graph-api/reference/waba-analytics/) | Used to designate which analytics metrics you want returned. See [Analytics](https://developers.facebook.com/docs/whatsapp/business-management-api/analytics). |
| `business_verification_status`<br><br>enum | Current status of business verification of Meta Business Account which owns this WhatsApp Business Account |
| `country`[](#)<br><br>string | country of the WhatsApp Business Account's owning Meta Business account |
| `currency`<br><br>string | The currency in which the payment transactions for the WhatsApp Business Account will be processed<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `is_enabled_for_insights`<br><br>bool | If `true`, indicates the WhatsApp Business Account enabled template analytics. See [Analytics](https://developers.facebook.com/docs/whatsapp/business-management-api/analytics). |
| `message_template_namespace`<br><br>string | Namespace string for the message templates that belong to the WhatsApp Business Account<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `name`<br><br>string | User-friendly name to differentiate WhatsApp Business Accounts<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `on_behalf_of_business_info`<br><br>WABAOnBehalfOfComputedInfo | The "on behalf of" information for the WhatsApp Business Account |
| `ownership_type`[](#)<br><br>enum | Ownership type of the WhatsApp Business Account |
| `primary_funding_id`<br><br>numeric string | Primary funding ID for the WhatsApp Business Account paid service |
| `purchase_order_number`<br><br>string | The purchase order number supplied by the business for payment management purposes |
| `timezone_id`<br><br>string | The timezone of the WhatsApp Business Account<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |