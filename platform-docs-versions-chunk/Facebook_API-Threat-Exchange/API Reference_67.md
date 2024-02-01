platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/submitting


## CSV examples

When you download as CSV, we put whitelist apps and privacy groups in the format `id1:name1;id2:name2`. Tags are always text-only, delimited by semicolons:

`id                 2494923897281868 td_description     This is an example descriptor td_status          UNKNOWN td_confidence      0 td_severity        SEVERE td_share_level     AMBER td_indicator_type  URI td_raw_indicator   https://evilevillabs.com/evil.php td_visibility      HAS_WHITELIST td_creation_time   2019-11-07T22:25:00-05:00 td_update_time     2019-11-07T22:25:01-05:00 td_expire_time td_owner_id        494491891138576 td_owner_name      Media Hash Sharing RF Test td_subjective_tags testing;pwny td_whitelist_apps  1064060413755420:Media Hash Sharing Test;494491891138576:Media Hash Sharing RF Test`
        

When upload from CSV, you may specify whitelist apps and privacy groups in the format `id1;id2` if you prefer:

`td_description     This is an example descriptor td_status          UNKNOWN td_confidence      0 td_severity        SEVERE td_share_level     AMBER td_indicator_type  URI td_raw_indicator   https://evilevillabs.com/evil.php td_visibility      HAS_WHITELIST td_creation_time   2019-11-07T22:25:00-05:00 td_update_time     2019-11-07T22:25:01-05:00 td_expire_time td_owner_id        494491891138576 td_owner_name      Media Hash Sharing RF Test td_subjective_tags testing;pwny td_whitelist_apps  1064060413755420;494491891138576`