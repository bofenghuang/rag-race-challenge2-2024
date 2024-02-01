platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/ad_studies/


### Parameters

| Parameter | Description |
| --- | --- |
| `cells`<br><br>list<Object> | A shape to describe the cells of the study |
| `description`<br><br>string |     |
| `id`<br><br>int64 |     |
| `name`<br><br>string |     |
| `creation_template`<br><br>enum {AUTOMATIC\_PLACEMENTS, BRAND\_AWARENESS, FACEBOOK, FACEBOOK\_AUDIENCE\_NETWORK, FACEBOOK\_INSTAGRAM, FACEBOOK\_NEWS\_FEED, FACEBOOK\_NEWS\_FEED\_IN\_STREAM\_VIDEO, IN\_STREAM\_VIDEO, INSTAGRAM, MOBILE\_OPTIMIZED\_VIDEO, PAGE\_POST\_ENGAGEMENT, REACH, TV\_COMMERCIAL, TV\_FACEBOOK, VIDEO\_VIEW\_OPTIMIZATION, LOW\_FREQUENCY, MEDIUM\_FREQUENCY, HIGH\_FREQUENCY} |     |
| `adaccounts`<br><br>list<int64> |     |
| `adsets`<br><br>list<numeric string or integer> |     |
| `campaigns`<br><br>list<numeric string or integer> |     |
| `control_percentage`<br><br>float with at most two digits after decimal point |     |
| `treatment_percentage`<br><br>float with at most two digits after decimal point |     |
| `client_business`<br><br>numeric string or integer | Business associated with study |
| `confidence_level`<br><br>float | Confidence level used in power calculation and final report |
| `cooldown_start_time`<br><br>integer | The beginning of the pre measurement cooldown period. This period ends when the study period starts. |
| `description`<br><br>string | A brief description about the purpose of the study. |
| `end_time`<br><br>integer | The time when the study period ends. |
| `name`<br><br>string | The name of the study. |
| `objectives`<br><br>list<Object> | A vector of objects describing the objectives assigned to this study |
| `id`<br><br>numeric string or integer |     |
| `is_primary`<br><br>boolean |     |
| `name`<br><br>string |     |
| `type`<br><br>enum {SALES, NONSALES, MAE, TELCO, FTL, MAI, PARTNER, BRANDLIFT, BRAND, MPC\_CONVERSION, CONVERSIONS} |     |
| `offsite_datasets`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `adspixels`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `customconversions`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `applications`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `offline_conversion_data_sets`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `product_sets`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `product_catalogs`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `observation_end_time`<br><br>integer | The end of the observation period for this study, this period starts when the study period ends. |
| `start_time`<br><br>integer | The time when the study period starts. |
| `type`<br><br>enum {LIFT, SPLIT\_TEST, CONTINUOUS\_LIFT\_CONFIG, GEO\_LIFT} | The type of ad study, either SPLIT\_TEST or LIFT. |
| `viewers`<br><br>list<int> | The list of people who this study has been shared with. |