platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/submitting


## Field names for upload

Bold parameters are required.

| API Name and Example | UI CSV Name and Example | Description |
| --- | --- | --- |
| **`access_token`**  <br>`555\|aSdF123GhK` | _Not used for the UI_ | The key for authenticating to the API, in the format<br><br>`your-app-id\|your-app-secret`  <br>  <br><br>Please visit the<br><br>[Access Token Tool](https://developers.facebook.com/tools/accesstoken)<br><br>to find values for your app(s). |
| **`description`**  <br>`This%20domain%20was%20hosting%20malware` | **`td_description`**  <br>`This domain was hosting malware` | A short summary of the indicator and threat. |
| **`indicator`**  <br>`evil-domain.biz` | **`td_raw_indicator`**  <br>`evil-domain.biz` | The indicator data being submitted. |
| **`type`**  <br>`URI` | **`td_indicator_type`**  <br>`URI` | The kind of indicator being described. See<br><br>[IndicatorType](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type)<br><br>for the list of allowed values. |
| **`privacy_type`**  <br>`HAS_PRIVACY_GROUP` | **`td_visibility`**  <br>`HAS_PRIVACY_GROUP` | The kind of privacy for the indicator. See<br><br>[PrivacyType](https://developers.facebook.com/docs/threat-exchange/reference/apis/privacy-type)<br><br>for the list of allowed values. |
| `privacy_members`  <br>`1064060413755420,494491891138576` | `td_whitelist_apps`  <br>`1064060413755420,494491891138576`  <br>  <br>`td_privacy_groups`  <br>`438835087026293,468692780520730`  <br>  <br><br>Or, for compatibility, you can use a column name of<br><br>`td_privacy_members`<br><br>for upload if you like. If visibility is HAS\_WHITELIST, we will proceed as if your td\_privacy\_members column were named td\_whitelist\_apps; if visibility is HAS\_PRIVACY\_GROUP, we will proceed as if your td\_privacy\_members column were named td\_privacy\_groups.<br><br>  <br>  <br><br>See [CSV examples](#csv_examples) and [JSON examples below.](#json_examples) | A list of<br><br>[ThreatExchangeMembers](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member)<br><br>allowed to see the indicator, and only applies when<br><br>`privacy_type`<br><br>is set to<br><br>`HAS_WHITELIST`<br><br>or<br><br>`HAS_PRIVACY_GROUP`<br><br>. Delimiters are comma for the API and semicolon for the UI. |
| **`share_level`**  <br>`AMBER` | **`td_share_level`**  <br>`AMBER` | A designation of how the indicator may be shared based on the<br><br>[US-CERT's Traffic Light Protocol](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.us-cert.gov%2Ftlp%2F&h=AT1lDi6RYilqHgZwrNBM_MJIZNzrTdESNhoP1JNTW0qpNQ1EaeE-M7LQq-RVoqNEd3nSh2syYmIQoqZ3yek27hCH18fcjpDwExikZpqyXnkWdKmjFguPNEGzsex3Gb-tdGPpxaeVhJ25zTPG)<br><br>. See<br><br>[ShareLevelType](https://developers.facebook.com/docs/threat-exchange/reference/apis/share-level-type)<br><br>for the list of allowed values. Note: GREEN/WHITE requires VISIBLE, and AMBER/RED requires HAS\_WHITELIST or HAS\_PRIVACY\_GROUP. |
| **`status`**  <br>`MALICIOUS` | **`td_status`**  <br>`MALICIOUS` | Indicates if the indicator is labeled as malicious. See<br><br>[StatusType](https://developers.facebook.com/docs/threat-exchange/reference/apis/status-type)<br><br>for the list of allowed values. |
| `tags`  <br>`testing,pwny` | `td_subjective_tags`  <br>`testing;pwny` | API: a comma-separated list of tags you want to publish. UI: a semicolon-separated list of tags you want to publish. This will replace any existing tags.  <br>Tags are not strictly required but do note that they are essential for your collaborators to discover data you contribute. |
| `add_tags`  <br>`pwny,testing` | _Not used for the UI_ | To add tags to an object without overwriting existing tags. |
| `remove_tags`  <br>`pwny,testing` | _Not used for the UI_ | Remove tags associated with an object. |
| `confidence`  <br>`100` | `td_confidence`  <br>`100` | A score for how likely the indicator's<br><br>`status`<br><br>is accurate, ranging from 0 to 100. |
| `expired_on` | `td_expire_time`  <br>`2019-11-07T22:25:00-05:00` | Time the indicator is no longer considered a threat, in ISO 8601 date format. |
| `first_active` | `td_first_active`  <br>`2019-11-07T22:25:00-05:00` | Time when the opinion first became valid. |
| `last_active` | `td_last_active`  <br>`2019-11-07T22:25:00-05:00` | Time when the opinion stopped being valid. |
| `review_status`  <br>`PENDING` | `td_review_status`  <br>`PENDING` | Describes how the indicator was vetted. See<br><br>[ReviewStatusType](https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type)<br><br>for the list of allowed values. |
| `severity`  <br>`SEVERE` | `td_severity`  <br>`SEVERE` | A rating of how severe the indicator is when found in an incident. See<br><br>[SeverityType](https://developers.facebook.com/docs/threat-exchange/reference/apis/severity-type)<br><br>for the list of allowed values. |
| N/A | `td_related_ids_for_upload` | For submitting relations in bulk. Please see the<br><br>[Submitting Connections page](https://developers.facebook.com/docs/threat-exchange/reference/submitting-connections)<br><br>for more information. |
| N/A | `td_related_triples_for_upload` | For submitting relations in bulk. Please see the<br><br>[Submitting Connections page](https://developers.facebook.com/docs/threat-exchange/reference/submitting-connections)<br><br>for more information. |