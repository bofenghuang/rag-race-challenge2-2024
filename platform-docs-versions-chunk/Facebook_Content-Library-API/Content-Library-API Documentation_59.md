platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/guide-ig-accounts


## search\_ig\_accounts() method

This is the syntax of the `search_ig_accounts()` method:

search\_ig\_accounts(
    q=Q,
    fields=FIELDS,
    account\_ids=ACCOUNT\_IDS,
    account\_types=ACCOUNT\_TYPES,
    is\_verified=IS\_VERIFIED,
    since=SINCE,
    until=UNTIL      
)

The following table describes the parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `Q`  <br>_Optional_ | String | Keyword(s) to search Instagram accounts for. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`  <br>_Optional_ | List | A comma-separated list of Instagram account fields you want included in search results. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-ig-account) for descriptions of all available fields. |
| `ACCOUNT_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library Instagram account IDs to include in the search results. Maximum of 250 IDs. |
| `ACCOUNT_TYPES`  <br>_Optional_ | List | Comma-separated list of account types of the Instagram accounts to be included in the search results. Possible values are `creator`, `business` and `personal`.<br><br>Public Instagram accounts include professional accounts for businesses and creators. They also include a subset of personal accounts that have privacy [set to public](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F517073653436611&h=AT35bM9jd4-51bPM-dSx0NBJ961SaJNjMPeCdTU2npg_1CV6LhbLtdivmsIlJsSZygReOQ2hbgRzyF1mG8E_ZSLuKhptc5GoTX2Afkm8UAJ33kpGXNxfejtSF7-gGQB_v_kqpsQo3zRjMwqz) and have either a verified badge or 50,000 or more followers. A [verified badge](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F733907830039577%3Fhelpref%3Dfaq_content&h=AT2wLuUfIfonVYEVbqVIxC1ig3EpytHQpIi4qNKY0UHz-vM5tm555Vtx7rgpIO5sFjSpX3nZ_kv2Hg_mA0m-JniKL_vBJ8XMMGXe8JKlsmmhYi3vpVZl1nuhfUC20yhNE1ORraGgX53--elS) in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription. |
| `IS_VERIFIED`  <br>_Optional_ | Boolean | Whether the Instagram account is verified. An Instagram account with a legacy blue verified badge means that Instagram has confirmed that it is the authentic presence for that person or brand. [Learn more](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F854227311295302&h=AT2g_GUGNTO7wifBolL_vycelEy3jnLBcSLWKwNJ8cp2x-FtnD1dwpJEcBgWFTDXOSfS_H86rupzk4rsM_jo6Bz4F1UnyF4zJbanhaVWrK7y48h3gzgumjI5pvVLPz67DkcxqH7hnOVhVjFu). |
| `SINCE`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Instagram accounts created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the account.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Instagram time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Instagram time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |
| `UNTIL`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Instagram accounts created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the account.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Instagram time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Instagram time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |