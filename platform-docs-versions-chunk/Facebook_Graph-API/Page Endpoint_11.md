platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/

### Parameters

| Parameter | Description |
| --- | --- |
| `api_version`<br><br>enum {} | api\_version |
| `custom_token`<br><br>string | An optional Wit token enable custom entities |
| `model`<br><br>enum {ARABIC, CHINESE, CROATIAN, CUSTOM, DANISH, DUTCH, ENGLISH, FRENCH\_STANDARD, GEORGIAN, GERMAN\_STANDARD, GREEK, HEBREW, HUNGARIAN, IRISH, ITALIAN\_STANDARD, KOREAN, NORWEGIAN\_BOKMAL, POLISH, PORTUGUESE, ROMANIAN, SPANISH, SWEDISH, VIETNAMESE} | An option for which model to use in production. |
| `n_best`<br><br>int64 | The number of intents and traits to return, other than the best one. |
| `nlp_enabled`<br><br>boolean | A boolean to enable/disable Built-In NLP. |
| `other_language_support`<br><br>JSON object {string : JSON object} | A map of language to model type and Wit token for language identification. |