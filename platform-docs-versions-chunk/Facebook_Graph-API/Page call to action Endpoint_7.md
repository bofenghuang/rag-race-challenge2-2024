platform: Facebook
topic: Graph-API
subtopic: Page call to action Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page call to action Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page-call-to-action/


### Parameters

| Parameter | Description |
| --- | --- |
| `android_app_id`<br><br>int | ID of the App that stores the destination info on Android |
| `android_destination_type`<br><br>enum {WEBSITE, APP\_DEEPLINK, FACEBOOK\_APP, PHONE\_CALL, MESSENGER, EMAIL, SHOP\_ON\_FACEBOOK, NONE, BECOME\_A\_VOLUNTEER, FOLLOW, MINI\_SHOP, MARKETPLACE\_INVENTORY\_PAGE, MOBILE\_CENTER, MENU\_ON\_FACEBOOK} | Destination type for the call-to-action on Android |
| `android_package_name`<br><br>string | Destination app for the call-to-action on Android |
| `android_url`<br><br>URL | Destination url for the call-to-action on Android |
| `email_address`<br><br>string | Email address that can be contacted by a user |
| `intl_number_with_plus`<br><br>string | International phone number with plus that can be called through a phone |
| `iphone_app_id`<br><br>int | ID fo the App that stores the destination info on iPhone |
| `iphone_destination_type`<br><br>enum {WEBSITE, APP\_DEEPLINK, FACEBOOK\_APP, PHONE\_CALL, MESSENGER, EMAIL, SHOP\_ON\_FACEBOOK, NONE, BECOME\_A\_VOLUNTEER, FOLLOW, MINI\_SHOP, MARKETPLACE\_INVENTORY\_PAGE, MENU\_ON\_FACEBOOK} | Destination type for the call-to-action on iPhone |
| `iphone_url`<br><br>URL | Destination url for the call-to-action on iPhone |
| `type`<br><br>enum {BOOK\_NOW, REQUEST\_QUOTE, CALL\_NOW, CHARITY\_DONATE, CONTACT\_US, DONATE\_NOW, MESSAGE, OPEN\_APP, PLAY\_NOW, SHOP\_NOW, SIGN\_UP, WATCH\_NOW, GET\_OFFER, GET\_OFFER\_VIEW, BOOK\_APPOINTMENT, LISTEN, EMAIL, LEARN\_MORE, REQUEST\_APPOINTMENT, GET\_DIRECTIONS, BUY\_TICKETS, PLAY\_MUSIC, VISIT\_GROUP, SHOP\_ON\_FACEBOOK, LOCAL\_DEV\_PLATFORM, INTERESTED, WOODHENGE\_SUPPORT, BECOME\_A\_VOLUNTEER, VIEW\_SHOP, PURCHASE\_GIFT\_CARDS, FOLLOW\_PAGE, ORDER\_FOOD, VIEW\_INVENTORY, MOBILE\_CENTER, VIEW\_MENU} | The type of action |
| `web_destination_type`<br><br>enum {EMAIL, MESSENGER, NONE, WEBSITE, SHOP\_ON\_FACEBOOK, BECOME\_SUPPORTER, BECOME\_A\_VOLUNTEER, FOLLOW, MOBILE\_CENTER} | Destination type for the call-to-action on desktop |
| `web_url`<br><br>URL | Destination url for the call-to-action on desktop |