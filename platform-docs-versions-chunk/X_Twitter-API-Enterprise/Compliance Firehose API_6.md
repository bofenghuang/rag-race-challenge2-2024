platform: X
topic: Twitter-API-Enterprise
subtopic: Compliance Firehose API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Compliance Firehose API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/compliance-firehose-api/guides/compliance-data-objects


## Payload examples

See the payload examples below for each compliance event described in the table above.

**Tweet edit**

      `{"tweet_edit":    {      "id": "1557445923210514432"      "initial_tweet_id": "1557433858676740098",      "edit_tweet_ids": ["1557433858676740098", "1557445923210514432"],      "timestamp_ms": "1660155761384"    }  }`
    

#### Tweet delete

      `{   "delete": {     "status": {       "id": 601430178305220600,       "id_str": "601430178305220608",       "user_id": 3198576760,       "user_id_str": "3198576760"     },     "timestamp_ms": "1432228155593"   } }`
    

#### Tweet withheld

      `{   "status_withheld": {     "status": {       "id": 601430178305220600,       "id_str": "601430178305220608",       "user_id": 3198576760,       "user_id_str": "3198576760"     },     "withheld_in_countries": [       "XY"     ],     "timestamp_ms": "1432228155593"   } }`
    

#### Drop

      `{   "drop": {     "status": {       "id": 601430178305220600,       "id_str": "601430178305220600",       "user_id": 3198576760,       "user_id_str": "3198576760"     },     "timestamp_ms": "1432228155593"   } }`
    

#### Undrop

      `{   "undrop": {     "status": {       "id": 601430178305220600,       "id_str": "601430178305220600",       "user_id": 3198576760,       "user_id_str": "3198576760"     },     "timestamp_ms": "1432228155593"   } }`
    

#### Scrub geo

      `{   "scrub_geo": {     "user_id": 519761961,     "up_to_status_id": 411552403083628540,     "up_to_status_id_str": "411552403083628544",     "user_id_str": "519761961",     "timestamp_ms": "1432228180345"   } }`
    

#### User delete

      `{   "user_delete": {     "id": 771136850,     "timestamp_ms": "1432228153548"   } }`
    

#### User undelete

      `{   "user_undelete": {     "id": 796250066,     "timestamp_ms": "1432228149062"   } }`
    

#### User withheld

      `{   "user_withheld": {     "user": {       "id": 1375036644,       "id_str": "1375036644"     },     "withheld_in_countries": [       "XY"     ],     "timestampMs": "2014-08-27T23:49:41.839+00:00"   } }`
    

#### User protect

      `{   "user_protect": {     "id": 3182003550,     "timestamp_ms": "1432228177137"   } }`
    

#### User unprotect

      `{   "user_unprotect": {     "id": 2911076065,     "timestamp_ms": "1432228180113"   } }`
    

#### User suspend

      `{   "user_suspend": {     "id": 3120539094,     "timestamp_ms": "1432228194217"   } }`
    

#### User unsuspend

      `{   "user_unsuspend": {     "id": 3293130873,     "timestamp_ms": "1432228193828"   } }`