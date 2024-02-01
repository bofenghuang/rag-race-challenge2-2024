platform: Facebook
topic: Graph-API
subtopic: Link Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Link Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/link

### Permissions

* Any valid access token if the link is public
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `id` | The link ID. | `string` |
| `created_time` | The time the message was published. | `datetime` |
| `description` | A description of the link (appears beneath the link caption). | `string` |
| `from` | The user that created the link. | [`User`](https://developers.facebook.com/docs/graph-api/reference/user) |
| `icon` | A URL to the link icon that Facebook displays in Feed. | `string` |
| `link` | The URL that was shared. | `string` |
| `message` | The optional message from the user about this link. | `string` |
| `name` | The name of the link. | `string` |
| `picture` | A URL to the thumbnail image used in the link post | `string` |
| `reactions`<br><br>  <br><br>Deprecated in v8.0+. | Reactions, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY, NONE, to a link. | `string` |