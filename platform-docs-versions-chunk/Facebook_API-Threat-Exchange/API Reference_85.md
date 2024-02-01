platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/submitting-connections


## Use the UI for Bulk Upload

These are optional columns you can use to bulk-relate (see also [Submit Data](https://developers.facebook.com/docs/threat-exchange/reference/submitting):

* The descriptors you want to relate your new one to must already exist.
* You can specify the relate-to descriptors by ID using the `td_related_ids_for_upload` column.
* Alternatively, you can specify the related-to descriptors using the `td_related_triples_for_upload` column. Provide the owner-app ID, indicator type, and indicator text, which will uniquely identify the linked-to descriptors.

#### CSV Example (written vertically for convenience):

`td_description                Testing bulk upload td_status                     NON_MALICIOUS td_confidence                 100 td_severity                   INFO td_share_level                AMBER td_indicator_type             HASH_MD5 td_raw_indicator              e8b19da37825a3056e84c522f05eb000 td_visibility                 HAS_WHITELIST td_subjective_tags            testing td_whitelist_apps             494491891138576:Media Hash Sharing RF Test td_privacy_groups              td_review_status              REVIEWED_MANUALLY td_related_ids_for_upload     2515798535123892,2376386079125415 td_related_triples_for_upload   td_description                Testing bulk upload td_status                     NON_MALICIOUS td_confidence                 100 td_severity                   INFO td_share_level                AMBER td_indicator_type             HASH_MD5 td_raw_indicator              e8b19da37825a3056e84c522f05eb001 td_visibility                 HAS_WHITELIST td_subjective_tags            pwny;testing td_whitelist_apps             494491891138576:Media Hash Sharing RF Test td_privacy_groups              td_review_status              REVIEWED_MANUALLY td_related_ids_for_upload      td_related_triples_for_upload 494491891138576:HASH_MD5:e8b19da37825a3056e84c522f05eb000,494491891138576:HASH_MD5:e8b19da37825a3056e84c522f05eb002`

#### JSON Example:

`[   {     "td_description": "Testing bulk upload/relate",     "td_status": "NON_MALICIOUS",     "td_confidence": 100,     "td_severity": "INFO",     "td_share_level": "AMBER",     "td_indicator_type": "HASH_MD5",     "td_raw_indicator": "e8b19da37825a3056e84c522f05eb000",     "td_visibility": "HAS_WHITELIST",     "td_subjective_tags": ["testing"],     "td_whitelist_apps": [       {         "id": "494491891138576",         "name": "Media Hash Sharing RF Test"       }     ],     "td_privacy_groups": [],     "td_review_status": "REVIEWED_MANUALLY",     "td_related_ids_for_upload": ["2515798535123892","2376386079125415"]   },   {     "td_description": "Testing bulk upload/relate",     "td_status": "NON_MALICIOUS",     "td_confidence": 100,     "td_severity": "INFO",     "td_share_level": "AMBER",     "td_indicator_type": "HASH_MD5",     "td_raw_indicator": "e8b19da37825a3056e84c522f05eb001",     "td_visibility": "HAS_WHITELIST",     "td_subjective_tags": ["pwny", "testing"],     "td_whitelist_apps": [       {         "id": "494491891138576",         "name": "Media Hash Sharing RF Test"       }     ],     "td_privacy_groups": [],     "td_review_status": "REVIEWED_MANUALLY",     "td_related_triples_for_upload": [       {         "owner_app_id": "494491891138576",         "td_indicator_type": "HASH_MD5",         "td_raw_indicator": "e8b19da37825a3056e84c522f05eb000"       },       {         "owner_app_id": "494491891138576",         "td_indicator_type": "HASH_MD5",         "td_raw_indicator": "e8b19da37825a3056e84c522f05eb002"       }     ]   } ]`