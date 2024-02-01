platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/activities/


### Parameters

| Parameter | Description |
| --- | --- |
| `advertiser_id`<br><br>string | Apple's Advertising Identifier (IDFA) or Google Android's advertising ID. You can see how Facebook fetches this on [iOS](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-ios-sdk%2Fblob%2F7fe08877ea773dc35a5e4d6d9d305fae57c513b6%2Fsrc%2FCore%2FFBUtility.m%23L334-L357&h=AT09cH5PlAYq7RlSWCvNBvWsJAD08TC3XTMYZyRKZe34Gj-ZIEI8c13BomKJAn9SltHsF-ruDFXvueCBhsPBJulXE1OH011MDjL2Wmwq5hYnSx4ZMin7a2wcAsbxrrdZcJfA9Usqqr_qbi7q) or on [Android](https://developers.facebook.com/docs/reference/ads-api/mobile-conversions-endpoint/v2.2#android) |
| `advertiser_tracking_enabled`<br><br>boolean | Specifies whether a person has enabled advertising tracking on their device. Set to 0 for disabled or 1 for enabled. You should fetch this data and return it to Meta will use the event data (from partners about user activities off Meta) pursuant to its Data Policy, including for ad reporting, fraud detection and to build and improve our products (including our ads delivery products), but will restrict use of data about that individual to personalize that user’s ads. For devices running earlier versions than iOS 6, this parameter should default to 1. |
| `anon_id`<br><br>string | The ID of a person who has installed the app anonymously |
| `app_user_id`<br><br>string | Specifies [user id](https://developers.facebook.com/docs/analytics/properties#user-id) of an app user. Used internally by the iOS and Android SDKs for `MOBILE_APP_INSTALL` event |
| `application_tracking_enabled`<br><br>boolean | A person can choose to enable ad tracking on an app level. Your SDK should allow an app developer to put an opt-out setting into their app. Use this field to specify the person's choice. Use 0 for disabled, 1 for enabled |
| `attribution`<br><br>string | mobile\_cookie from the person's device. Use this only on Android or iOS devices before iOS 6. The format for this should look something like `DDDECD0A-C076-4050-8CE8-C20EC3FC2BD3` |
| `auto_publish`<br><br>boolean | This field is not longer being used. Used to be used internally by Facebook's SDK |
| `bundle_id`<br><br>string | Used internally by Facebook's SDK |
| `bundle_short_version`<br><br>string | Used internally by Facebook's SDK |
| `bundle_version`<br><br>string | Used internally by Facebook's SDK |
| `campaign_ids`<br><br>string | Parameter passed via the deep link for Mobile App Engagement campaigns. |
| `click_id`<br><br>string | click\_id |
| `consider_views`<br><br>boolean | Specifies that view through data should be considered when determining the ad to attribute this install to. Clicks will always be considered first before views and views will only be returned if there was not a click on an ad for the app |
| `custom_events`<br><br>list<CustomEvent> | Custom events reported, required with `CUSTOM_APP_EVENTS` events. Please see our [App Events API](https://developers.facebook.com/docs/marketing-api/app-event-api), [App Events for iOS](https://developers.facebook.com/docs/app-events/ios) and [App Events for Android](https://developers.facebook.com/docs/app-events/android) for more information |
| `_eventName`<br><br>RegexParam | Event name, must match the regular expression /^\[0-9a-zA-Z\_\]\[0-9a-zA-Z \_-\]{0,39}$/<br><br>Required |
| `_eventName_md5`<br><br>RegexParam | MD5 hash of the event name, must match the regular expression /^\[A-Fa-f0-9\]{32}$/ |
| `_valueToSum`<br><br>float | Values to Sum |
| `_logTime`<br><br>int64 | Time to Log |
| `_implicitlyLogged`<br><br>int64 | Whether this is implicitly logged |
| `_isTimedEvent`<br><br>boolean | Whether this is a timed event |
| `_session_id`<br><br>string |     |
| `_app_user_id`<br><br>string |     |
| `custom_events_file`<br><br>file | Custom file, encoded as JSON that describes the event. Please encode as UTF-8 and attach with the mime type `application/json` or `content/unknown` |
| `device_token`<br><br>string | A token used to identify the device on push networks |
| `event`<br><br>enum {MOBILE\_APP\_INSTALL, CUSTOM\_APP\_EVENTS, DEFERRED\_APP\_LINK} | Event type, one of `MOBILE_APP_INSTALL`, `CUSTOM_APP_EVENTS` or `DEFERRED_APP_LINK`. If you are reporting a `MOBILE_APP_INSTALL` event, you must include either `attribution` or `advertiser_id` in the request<br><br>Required |
| `extinfo`<br><br>Object | Extended device and source information array, used by Facebook's SDKs, MMPs and Bots for Messenger. This parameter is an array and must be in a specific format. Please see our [App Events API](https://developers.facebook.com/docs/marketing-api/app-event-api) for more information |
| `0`<br><br>string | extinfo version<br><br>Required |
| `1`<br><br>string | app package name |
| `2`<br><br>string | short version (int or string) |
| `3`<br><br>string | long version |
| `4`<br><br>string | OS version |
| `5`<br><br>string | device model name |
| `6`<br><br>string | locale |
| `7`<br><br>string | timezone abbreviation |
| `8`<br><br>string | carrier |
| `9`<br><br>int64 | screen width |
| `10`<br><br>int64 | screen height |
| `11`<br><br>string | screen density (float decimal , or .) |
| `12`<br><br>int64 | CPU cores |
| `13`<br><br>int64 | external storage size in GB |
| `14`<br><br>int64 | free space on external storage in GB |
| `15`<br><br>string | device timezone |
| `include_dwell_data`<br><br>boolean | Specifies that view dwell ms should be returned as part of view through data |
| `include_video_data`<br><br>boolean | Specifies that video view completion percentages should be returned as part of view through data |
| `install_referrer`<br><br>string | 3rd party install referrer, currently available for Android only, see https://developers.google.com/analytics/devguides/collection/android/v4/campaigns |
| `installer_package`<br><br>string | Used internally by the Android SDKs |
| `migration_bundle`<br><br>string | Used internally by the iOS and Android SDKs |
| `page_id`<br><br>int64 | Specifies the Page ID associated with the messenger bot that logs the event |
| `page_scoped_user_id`<br><br>int64 | Specifies the page scoped User ID associated with the messenger bot that logs the event |
| `receipt_data`<br><br>string | The receipts of in-app purchase |
| `ud`<br><br>JSON object | Optional user data parameters for advanced matchingProvide hashed fields as key/value pairs similar to the Pixel |
| `em`<br><br>string | em  |
| `fn`<br><br>string | fn  |
| `ln`<br><br>string | ln  |
| `ph`<br><br>string | ph  |
| `ge`<br><br>string | ge  |
| `dob`<br><br>string | dob |
| `ct`<br><br>string | ct  |
| `st`<br><br>string | st  |
| `zp`<br><br>string | zp  |
| `extern_id`<br><br>string | extern\_id |
| `db`<br><br>string | db  |
| `r1`<br><br>string | r1  |
| `r2`<br><br>string | r2  |
| `cn`<br><br>string | cn  |
| `r3`<br><br>string | r3  |
| `r4`<br><br>string | r4  |
| `r5`<br><br>string | r5  |
| `r6`<br><br>string | r6  |
| `r7`<br><br>string | r7  |
| `r8`<br><br>string | r8  |
| `country`<br><br>string | country |
| `external_id`<br><br>string | external\_id |
| `url_schemes`<br><br>list<string> | Used internally by the iOS and Android SDKs |
| `user_id`<br><br>string | user\_id |
| `user_id_type`<br><br>enum {INSTANT\_GAMES\_PLAYER\_ID} | user\_id\_type |
| `vendor_id`<br><br>string | vendor\_id |
| `windows_attribution_id`<br><br>string | Attribution token used for Windows 10 |