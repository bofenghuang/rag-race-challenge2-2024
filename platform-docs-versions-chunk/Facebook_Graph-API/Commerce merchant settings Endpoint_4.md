platform: Facebook
topic: Graph-API
subtopic: Commerce merchant settings Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Commerce merchant settings Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | ID of the Commerce Merchant Settings |
| `braintree_merchant_id`<br><br>string | The Braintree Merchant ID (for BigCommerce) |
| `checkout_message`<br><br>string | Checkout Message of Commerce Merchant Settings<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `contact_email`<br><br>string | Contact email of Commerce Merchant Settings<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `cta`<br><br>enum | Shop's CTA (ie. onsite checkout, offsite, or contact-merchant) |
| `disable_checkout_urls`<br><br>bool | Ignore checkout\_urls for offsite links forthis merchant, if they exist on products. |
| `display_name`<br><br>string | Business display name |
| `external_merchant_id`<br><br>string | Merchant Identifier on External Partner Platforms (i.e. Shopify) |
| `facebook_channel`[](#)<br><br>CommerceFacebookChannel | Facebook channel settings |
| `feature_eligibility`<br><br>CommerceMerchantSettingsFeatureEligibility | Returns feature eligibilities for the Commerce Merchant Settings |
| `has_discount_code`<br><br>bool | Whether or not this merchant has discount code |
| `has_onsite_intent`<br><br>bool | This merchant selected onsite checkout during setup |
| `instagram_channel`[](#)<br><br>CommerceInstagramChannel | Instagram channel settings |
| `merchant_alert_email`<br><br>string | Place to send alert emails for the merchant |
| `merchant_page`<br><br>[Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) | Profile of the merchant selling products<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `merchant_status`<br><br>enum | Current status of the merchant |
| `onsite_commerce_merchant`<br><br>CommerceMerchantSettingsOnsiteCommerceMerchant | Commerce Merchant Settings Info for the new commerce platform API |
| `payment_provider`<br><br>enum | Payment Provider for Commerce Merchant Settings<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `privacy_url_by_locale`<br><br>list<KeyValue:string,string> | Map from locale to merchant privacy policy url. The locale follows the format of concatenating ISO language and country code with an underscore. For instance, en\_US represents U.S. English. |
| `review_rejection_messages`<br><br>list<string> | Descriptive rejection messages corresponding to the given rejection reasons, if applicable |
| `review_rejection_reasons`<br><br>list<enum> | Reasons the merchant was rejected on review (for onboarding requests or performance metrics), if applicable |
| `supported_card_types`<br><br>list<enum> | Credit card types supported by the merchant |
| `terms`<br><br>string | Terms of Commerce Merchant Settings<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `terms_url_by_locale`<br><br>list<KeyValue:string,string> | Map from locale to merchant terms url. The locale follows the format of concatenating ISO language and country code with an underscore. For instance, en\_US represents U.S. English. |
| `whatsapp_channel`[](#)<br><br>CommerceWhatsAppChannel | WhatsApp Channel Settings |