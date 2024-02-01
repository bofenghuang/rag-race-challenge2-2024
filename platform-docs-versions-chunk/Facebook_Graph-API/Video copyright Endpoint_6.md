platform: Facebook
topic: Graph-API
subtopic: Video copyright Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video copyright Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video-copyright/


### Parameters

| Parameter | Description |
| --- | --- |
| `append_excluded_ownership_segments`<br><br>boolean | If true, append the excluded ownership segments instead of replacing them |
| `attribution_id`<br><br>numeric string or integer | The ID of the attribution to be displayed for valid monitored videos matching this content. |
| `content_category`<br><br>enum {episode, movie, web} | The content category of the copyrighted reference file. |
| `excluded_ownership_countries`<br><br>list<UTF-8 encoded string> | A string array of [ISO 3166 format country codes](http://l.facebook.com/l.php?u=http%3A%2F%2Fwww.iso.org%2Fiso%2Fcountry_codes%2Fiso_3166_code_lists%2Fcountry_names_and_code_elements.htm&h=AT3N0plpn845_3n1WESaRUTGS2sUxFHCxyEXmWutd_Gk9h1G1urdV69aZUfuOkqtr5BWaA_4HBQc9Ojb5yRFhmy6O_DlV0omMAMPFe9UOZbDtCvWWwAm6yiWpKmf9SYtmx3ln7koxqN99DzJ), where the owner does not own the rights to the content |
| `excluded_ownership_segments`<br><br>list<Video Match Segment> | An array of match segments to exclude from the matching algorithm. System generated excluded segments may not be replaced. |
| `start_time_in_sec`<br><br>float | Required |
| `media_type`<br><br>enum {VIDEO\_AND\_AUDIO, VIDEO\_ONLY, AUDIO\_ONLY} | Required |
| `duration_in_sec`<br><br>float | Required |
| `segment_source`<br><br>enum {PUBLISHER\_DEFINED, PAUSE\_LIVE\_MONITORING, LABEL\_MUTED, PUBLISHER\_MUTED, MUSIC\_RESTRICTION\_MUTED\_STILL\_VIDEO, MUSIC\_RESTRICTION\_MUTED\_MULTI\_TRACK, AUDIO\_LIBRARY\_USAGE, MELODY, INELIGIBLE\_CONTENT} | Default value: `PUBLISHER_DEFINED` |
| `is_reference_disabled`<br><br>boolean | If true, stop creating matches for the reference file. |
| `monitoring_type`<br><br>enum {VIDEO\_AND\_AUDIO, VIDEO\_ONLY, AUDIO\_ONLY} | Setting to indicate whether the content has copyright ownership on video, audio, or both. |
| `ownership_countries`<br><br>list<UTF-8 encoded string> | A string array of [ISO 3166 format country codes](http://l.facebook.com/l.php?u=http%3A%2F%2Fwww.iso.org%2Fiso%2Fcountry_codes%2Fiso_3166_code_lists%2Fcountry_names_and_code_elements.htm&h=AT1ov9V4j-_SCXNokaqepVrl4aYDdN3I-qYWigLqshtNvsPBJR3ljjdFxTt8-hwSiYfu2ectDQ6IxCnpaOgw5B-8LLaUPzf81XpoyW5RWFsFv0bv4ORc4FEcTfVEbgkE4Xks5nzm3LVlT5uD), where the owner owns the rights to the content |
| `rule_id`<br><br>numeric string or integer | A copyright policy to be applied to the copyrighted content. |
| `whitelisted_ids`<br><br>list<numeric string> | A list of page IDs or user IDs, who are allowed to use the copyrighted content. |
| `whitelisted_ig_user_ids`<br><br>list<numeric string> | A list of Instagram user IDs who are allowed to use the copyrighted content. |