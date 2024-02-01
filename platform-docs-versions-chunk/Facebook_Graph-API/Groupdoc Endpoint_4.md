platform: Facebook
topic: Graph-API
subtopic: Groupdoc Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Groupdoc Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/groupdoc

### Fields

| Property Name | Description | Type |
| --- | --- | --- |
| `id` | The group doc ID. | `string` |
| `from` | The profile that created this doc. | [`User`](https://developers.facebook.com/docs/graph-api/reference/user/)`\|`[`Page`](https://developers.facebook.com/docs/graph-api/reference/page/) |
| `subject` | The title of the doc. | `string` |
| `message` | The body of the doc. This string will contain HTML for any formatting in the doc, and will be HTML encoded. | `string` |
| `icon` | The URL for the doc's icon | `string` |
| `created_time` | When the doc was created. | `datetime` |
| `updated_time` | The last time the doc was changed. | `datetime` |
| `revision` | An ID representing the current doc revision. | `int` |
| `can_edit` | Whether the session user can edit this doc. | `boolean` |
| `can_delete` | Whether the session user can delete this doc (on Facebook.com). | `boolean` |
| `embedded_urls` | URLs for document embeds | `[string]` |