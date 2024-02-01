platform: Facebook
topic: Graph-API
subtopic: Url Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Url Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/url


### Fields

| Property Name | Description | Type |
| --- | --- | --- |
| `app_links` | AppLinks data associated with this URL, if available. | `AppLinks` |
| `id` | The URL itself. | `string` |
| `engagement` | Counts of different ways people interacted with the URL Note that engagement values are intentionally not precise, but you can be confident they accurately reflect user engagement with a URL. | `object` |
| `comment_count` | Number of comments on the URL. | `int` |
| `comment_plugin_count` | Number of comments on the plugin gathered using the [Comments Plugin](https://developers.facebook.com/docs/plugins/comments/) on your site. | `int` |
| `reaction_count` | Number of reactions to the URL. | `int` |
| `share_count` | Number of times the URL was shared. | `int` |
| `og_object` | The [Open Graph object](https://developers.facebook.com/docs/opengraph/using-objects#selfhosted-canonical) that is canonically associated with this URL. | `OGObject` |
| `id` | ID of object. | `string` |
| `description` | The description of the object, if available. | `string` |
| `title` | The title of the object, if available. | `string` |
| `type` | The object type. | [`og:type`](https://developers.facebook.com/docs/opengraph/creating-custom-stories#objecttypes) |
| `updated_time` | When the object was last updated. | `datetime` |