platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/


### Parameters

| Parameter | Description |
| --- | --- |
| `payload`<br><br>Object | Payload representing users to add |
| `schema`<br><br>string | `EMAIL_SHA256`, `PHONE_SHA256`, `MOBILE_ADVERTISER_ID`. One can also pass an array of multiple keys for multi-key match. Supported key types includes:  <br>`EXTERN_ID`  <br>`EMAIL`  <br>`PHONE`  <br>`GEN`  <br>`DOBY`  <br>`DOBM`  <br>`DOBD`  <br>`LN`  <br>`FN`  <br>`FI`  <br>`CT`  <br>`ST`  <br>`ZIP`  <br>`MADID`  <br>`COUNTRY`  <br>The multi-key array is of the form `["EMAIL", "LN", "FN", "ZIP"]` |
| `is_raw`<br><br>boolean | Is the key raw? If the keys are combinational keys like "LN\_FN\_ZIP", set this to `false`, otherwise set this to `true`. Default to false |
| `data`<br><br>list<JSON array> | Array with users data. If the multi-key feature is used, a two-dimensional array of the form `[["<HASHED_EMAIL>", "<HASHED_FN>", "<HASHED_LN>", "<HASHED_ZIP>"], ["", "<HASHED_FN>", "<HASHED_LN>", "<HASHED_ZIP>"]]` should be passed.In case a key is unknown, it should be left blank. |
| `app_ids`<br><br>list<int> | App ids used by the users being uploaded. This field is required when `schema` is a Facebook UID and the IDs were collected by an App integration. e.g. `[1234,5678]` |
| `page_ids`<br><br>list<Page ID> | Page ids used by the users being uploaded. This field is required when `schema` is a Facebook UID and the IDs were collected by a Page webhook integration. e.g. `[1234,5678]` |
| `data_source`<br><br>Object | Indicates by which method the custom audience was created, defined by the `type` and `subtype` of the `data_source` |
| `type`<br><br>enum {UNKNOWN, FILE\_IMPORTED, EVENT\_BASED, SEED\_BASED, THIRD\_PARTY\_IMPORTED, COPY\_PASTE, CONTACT\_IMPORTER, HOUSEHOLD\_AUDIENCE} | Type of the custom audience |
| `sub_type`<br><br>enum {ANYTHING, NOTHING, HASHES, USER\_IDS, HASHES\_OR\_USER\_IDS, MOBILE\_ADVERTISER\_IDS, EXTERNAL\_IDS, MULTI\_HASHES, TOKENS, EXTERNAL\_IDS\_MIX, HOUSEHOLD\_EXPANSION, SUBSCRIBER\_LIST, WEB\_PIXEL\_HITS, MOBILE\_APP\_EVENTS, MOBILE\_APP\_COMBINATION\_EVENTS, VIDEO\_EVENTS, WEB\_PIXEL\_COMBINATION\_EVENTS, PLATFORM, MULTI\_DATA\_EVENTS, IG\_BUSINESS\_EVENTS, STORE\_VISIT\_EVENTS, INSTANT\_ARTICLE\_EVENTS, FB\_EVENT\_SIGNALS, ENGAGEMENT\_EVENT\_USERS, FACEBOOK\_WIFI\_EVENTS, AR\_EXPERIENCE\_EVENTS, AR\_EFFECTS\_EVENTS, MESSENGER\_ONSITE\_SUBSCRIPTION, CUSTOM\_AUDIENCE\_USERS, PAGE\_FANS, CONVERSION\_PIXEL\_HITS, APP\_USERS, S\_EXPR, DYNAMIC\_RULE, CAMPAIGN\_CONVERSIONS, WEB\_PIXEL\_HITS\_CUSTOM\_AUDIENCE\_USERS, MOBILE\_APP\_CUSTOM\_AUDIENCE\_USERS, COMBINATION\_CUSTOM\_AUDIENCE\_USERS, VIDEO\_EVENT\_USERS, FB\_PIXEL\_HITS, IG\_PROMOTED\_POST, PLACE\_VISITS, OFFLINE\_EVENT\_USERS, EXPANDED\_AUDIENCE, SEED\_LIST, PARTNER\_CATEGORY\_USERS, PAGE\_SMART\_AUDIENCE, MULTICOUNTRY\_COMBINATION, PLATFORM\_USERS, MULTI\_EVENT\_SOURCE, SMART\_AUDIENCE, LOOKALIKE\_PLATFORM, SIGNAL\_SOURCE, MAIL\_CHIMP\_EMAIL\_HASHES, CONSTANT\_CONTACTS\_EMAIL\_HASHES, COPY\_PASTE\_EMAIL\_HASHES, CUSTOM\_DATA\_TARGETING, CONTACT\_IMPORTER, DATA\_FILE} | Subtype of the custom audience |
| `metadata`<br><br>Object |     |
| `calculated_date`<br><br>datetime |     |
| `schema_version`<br><br>string |     |
| `session`<br><br>Object | Information about the session. Sessions are used when you have a lot of users to upload. For example, if you have 1 million users to upload, you need to split them into at least 100 requests because each request can only take 10k users. Specify the session info so that you can track if the session has finished or not. |
| `session_id`<br><br>int64 | Advertiser generated session identifier, used to track the session. Needs to be unique in the same ad account. |
| `estimated_num_total`<br><br>int64 | Estimated total num of users to be uploaded in this session, used by Facebook systems to better process this session. |
| `batch_seq`<br><br>int64 | A 1 based sequence number to identify the request in the session. |
| `last_batch_flag`<br><br>boolean | `true` mean this request is the last request in this session. You must mark the last request otherwise Facebook doesn't know the session has ended |