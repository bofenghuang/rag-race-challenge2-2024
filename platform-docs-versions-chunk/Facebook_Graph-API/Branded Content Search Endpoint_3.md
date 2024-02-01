platform: Facebook
topic: Graph-API
subtopic: Branded Content Search Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Branded Content Search Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/branded_content_search/

### Parameters

| Parameter | Description |
| --- | --- |
| `creation_date_max`<br><br>string | Search for branded content posted after the date (inclusive) you provide. The date format should be YYYY-mm-dd.<br><br>Required |
| `creation_date_min`<br><br>string | Search for branded content posted before the date (inclusive) you provide. The date format should be YYYY-mm-dd.<br><br>Required |
| `ig_username`<br><br>string | Search for an Instagram account that posted branded content or was a brand partner. Your search must include this parameter or page\_url. |
| `page_url`<br><br>URI | Search for a Facebook Page that posted branded content or was a brand partner. Your search must include this parameter or ig\_username. |