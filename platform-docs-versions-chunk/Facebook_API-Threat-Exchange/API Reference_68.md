platform: Facebook
topic: API-Threat-Exchange
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_API-Threat-Exchange/API Reference.md
url: https://developers.facebook.com/docs/threat-exchange/reference/submitting


## JSON examples

When you download as JSON, we put whitelist app, privacy groups, and tags in nested ID/name pairs:

`{   "id": "2699570156799349",   "td_description": "Testing bulk upload",   "td_status": "NON_MALICIOUS",   "td_confidence": 100,   "td_severity": "UNKNOWN",   "td_share_level": "AMBER",   "td_creation_time": 1575824153,   "td_update_time": 1575824154,   "td_expire_time": 0,   "td_indicator_type": "HASH_MD5",   "td_raw_indicator": "e8b19da37825a3056e84c522f05ed0c0",   "td_owner": {     "id": "1064060413755420",     "name": "Media Hash Sharing Test"   },   "td_subjective_tags": [     {       "id": "2055943881194599",       "td_name": "pwny"     },     {       "id": "1977957082312815",       "td_name": "testing"     }   ],   "td_visibility": "HAS_WHITELIST",   "td_whitelist_apps": [     {       "id": "1064060413755420",       "name": "Media Hash Sharing Test"     },     {       "id": "494491891138576",       "name": "Media Hash Sharing RF Test"     }   ],   "td_privacy_groups": [] }`
        

When you upload from JSON, if you prefer, you can write whitelist apps and privacy groups as simply arrays of IDs, and tags as arrays of text:

`{   "td_description": "This is an example descriptor",   "td_status": "UNKNOWN",   "td_confidence": 0,   "td_severity": "SEVERE",   "td_share_level": "AMBER",   "td_creation_time": 1573183500,   "td_update_time": 1573183501,   "td_expire_time": 0,   "td_indicator_type": "URI",   "td_raw_indicator": "https://evilevillabs.com/evil.php",   "td_subjective_tags": ["testing", "pwny"],   "td_visibility": "HAS_WHITELIST",   "td_whitelist_apps": ["1064060413755420", "494491891138576"] }`
        

See also the [Submitting Connections page](https://developers.facebook.com/docs/threat-exchange/reference/submitting-connections) for how to do related descriptors at bulk-upload.