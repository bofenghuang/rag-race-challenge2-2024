platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/mmp_auditing/


### Parameters

| Parameter | Description |
| --- | --- |
| `advertiser_id`<br><br>string | Apple's Advertising Identifier (IDFA) or Google Android's advertising ID. You can see how Facebook fetches this on [iOS](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-ios-sdk%2Fblob%2F7fe08877ea773dc35a5e4d6d9d305fae57c513b6%2Fsrc%2FCore%2FFBUtility.m%23L334-L357&h=AT1MbbkLIvVhl8ibHDPI6ZnEhqu0BIU_MaBjfSefSafi3gIpa_E877cjOplmYr5vhyhLWoQJRwxsPPQ07VR_wlDaHV4w6ZL1llyDviUqqgUfeNYNLiIbJ8OulyaCBz_w-Gx3HsG8pa0znRUc) or on [Android](https://developers.facebook.com/docs/reference/ads-api/mobile-conversions-endpoint/v2.2#android) |
| `attribution`<br><br>string | mobile\_cookie from the person's device. Use this only on Android or iOS devices before iOS 6. The format for this should look something like `DDDECD0A-C076-4050-8CE8-C20EC3FC2BD3` |
| `attribution_model`<br><br>string | attribution model that clients selected to be respected by MMP |
| `auditing_token`<br><br>string | Token provided in claim response sent to MMP |
| `click_attr_window`<br><br>int64 | Time window of click attribution |
| `custom_events`<br><br>list<CustomEvent> | Custom app events that MMP are sending auditing events for |
| `_eventName`<br><br>RegexParam | Event name, must match the regular expression /^\[0-9a-zA-Z\_\]\[0-9a-zA-Z \_-\]{0,39}$/<br><br>Required |
| `_eventName_md5`<br><br>RegexParam | MD5 hash of the event name, must match the regular expression /^\[A-Fa-f0-9\]{32}$/ |
| `_valueToSum`<br><br>float | Values to Sum |
| `_logTime`<br><br>int64 | Time to Log |
| `_implicitlyLogged`<br><br>int64 | Whether this is implicitly logged |
| `_isTimedEvent`<br><br>boolean | Whether this is a timed event |
| `_session_id`<br><br>string |     |
| `_app_user_id`<br><br>string |     |
| `decline_reason`<br><br>string | Reason that MMP rejected Facebook ads claim |
| `engagement_type`<br><br>string | Engagement type that MMP explicitly reports |
| `event`<br><br>string | Event type that Facebook claimed for<br><br>Required |
| `event_reported_time`<br><br>int64 | Time that event reported to MMP |
| `fb_ad_id`<br><br>int64 | FBID of the ads in Facebook claim<br><br>Required |
| `fb_click_time`<br><br>int64 | Ad click time in Facebook claim |
| `fb_view_time`<br><br>int64 | Ad view time in Facebook claim |
| `is_fb`<br><br>boolean | Result that whether MMP attribute the event to Facebook ads<br><br>Required |
| `used_install_referrer`<br><br>boolean | Identifies whether MMP used the install referrer |
| `view_attr_window`<br><br>int64 | Time window of view attribution |