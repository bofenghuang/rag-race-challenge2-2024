platform: Facebook
topic: Graph-API
subtopic: Place topic Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Place topic Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/place-topic/

### Parameters

| Parameter | Description |
| --- | --- |
| `icon_size`<br><br>enum{24, 36, 48, 72} | The size of the icon to get, one of 36, 48, or 72 |

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The topic ID |
| `count`<br><br>unsigned int32 | How many Pages have this category |
| `has_children`<br><br>bool | Whether there are subcategories of this category |
| `icon_url`<br><br>string | The URL for the icon representing this category |
| `name`<br><br>string | Localized name of the category<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `parent_ids`<br><br>list<id> | IDs of any parent categories that this is a subcategory of |
| `plural_name`<br><br>string | Localized plural name of the category |
| `top_subtopic_names`<br><br>list<string> | Names of the subtopics associated with the most pages |