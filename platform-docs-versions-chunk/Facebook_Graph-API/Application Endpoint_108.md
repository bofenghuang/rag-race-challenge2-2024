platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/application/page_activities/


### Parameters

| Parameter | Description |
| --- | --- |
| `advertiser_tracking_enabled`<br><br>boolean | A person can choose to enable ad tracking on iOS 6+, and that choice is stored within the phone. You should fetch that and return it to Facebook so we know not to use the data for optimization. We will, however, use the data to report on a conversion. See [here](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-ios-sdk%2Fblob%2F7fe08877ea773dc35a5e4d6d9d305fae57c513b6%2Fsrc%2FCore%2FFBUtility.m%23L334-L357&h=AT3SPxH_uzrP7bJw3DLR3Pv7COlVtyBjOLesmo_0nPuJo3BhwoaJAXbdLvlmMFYopzuf12UALtBc8VRE1B9tfrWscH_OmtV6kIS3H_IIRcs1QMYfjpUsIveemkkqIAL8POEFGxjFh0_k7GKP) for an example of how Facebook fetches that variable. For devices running less than iOS 6, this query parameter can default to 1. Use 0 for disabled, 1 for enabled |
| `application_tracking_enabled`<br><br>boolean | A person can choose to enable ad tracking on an app level. Your SDK should allow an app developer to put an opt-out setting into their app. Use this field to specify the person's choice. Use 0 for disabled, 1 for enabled |
| `custom_events`<br><br>list<CustomEvent> | Custom events reported |
| `_eventName`<br><br>RegexParam | Event name, must match the regular expression /^\[0-9a-zA-Z\_\]\[0-9a-zA-Z \_-\]{0,39}$/<br><br>Required |
| `_eventName_md5`<br><br>RegexParam | MD5 hash of the event name, must match the regular expression /^\[A-Fa-f0-9\]{32}$/ |
| `_valueToSum`<br><br>float | Values to Sum |
| `_logTime`<br><br>int64 | Time to Log |
| `_implicitlyLogged`<br><br>int64 | Whether this is implicitly logged |
| `_isTimedEvent`<br><br>boolean | Whether this is a timed event |
| `_session_id`<br><br>string |     |
| `_app_user_id`<br><br>string |     |
| `logging_source`<br><br>enum {MESSENGER\_BOT, DETECTION} | Specifies the event source |
| `logging_target`<br><br>enum {APP, APP\_AND\_PAGE, PAGE} | Default value: `"APP"`<br><br>whether the event is logged to app level or page level or both |
| `page_id`<br><br>int64 | Specifies the Page ID associated with the messenger bot that logs the event |
| `page_scoped_user_id`<br><br>int64 | Specifies the page scoped User ID associated with the messenger bot that logs the event<br><br>Required |