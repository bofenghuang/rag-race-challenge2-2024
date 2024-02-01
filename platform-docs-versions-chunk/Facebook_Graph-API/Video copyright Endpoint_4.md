platform: Facebook
topic: Graph-API
subtopic: Video copyright Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Video copyright Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/video-copyright/


### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The video copyright ID<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `content_category`<br><br>enum | The content category of the reference file.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `copyright_content_id`<br><br>numeric string | The copyright content ID<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `creator`<br><br>[User](https://developers.facebook.com/docs/graph-api/reference/user/) | The account that created the copyright<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `excluded_ownership_segments`<br><br>list<VideoCopyrightSegment> | The list of audio and video segments excluded from copyright monitoring. This includes both self-defined excluded segments as well as system generated excluded segments. |
| `in_conflict`<br><br>bool | Whether the video copyright is in active conflict with another rights owner's video copyright.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `monitoring_status`<br><br>enum | Whether the video is monitored successfully for copyright. The status could be NOT\_EXAMINED, COPYRIGHTED, and ERROR.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `monitoring_type`<br><br>enum | Whether the video is monitored for VIDEO, AUDIO, or VIDEO\_AND\_AUDIO<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `ownership_countries`<br><br>VideoCopyrightGeoGate | Two string arrays of [ISO 3166 format country codes](http://l.facebook.com/l.php?u=http%3A%2F%2Fwww.iso.org%2Fiso%2Fcountry_codes%2Fiso_3166_code_lists%2Fcountry_names_and_code_elements.htm&h=AT35FhNVNIIMHiPSM7VqW_So1AnusbmiaTJuENUa7wk5_rzcERJ0huReUEBPNf7jNzdeFbeti35cUn1zmRM_Ls9X9LZhGxCsXXjsxME-tqgy2g4xBVw-IX5IM5wvQvqNb2128NOWh3_k0BO0). `included_countries` are where the owner owns the rights to the content. `excluded_countries` are where the owner does not own the rights to the content. When both lists are empty, rights ownership is worldwide.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `reference_file`<br><br>CopyrightReferenceContainer | The reference file<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `reference_file_disabled`<br><br>bool | Whether the reference file is disabled.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `reference_file_disabled_by_ops`<br><br>bool | Whether the reference file has been disabled by ops.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `reference_owner_id`<br><br>string | The ID of the reference video owner<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `rule_ids`<br><br>[list<VideoCopyrightRule>](https://developers.facebook.com/docs/graph-api/reference/video-copyright-rule/) | A list of matching rules applied to the copyrighted content<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `tags`<br><br>list<string> | The tags/keywords associated with the copyright |
| `whitelisted_ids`<br><br>list<numeric string> | A list of page IDs or user IDs, who are allowed to use the copyrighted content.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |