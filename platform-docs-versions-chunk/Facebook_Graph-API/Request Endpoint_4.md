platform: Facebook
topic: Graph-API
subtopic: Request Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Request Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/request

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `id` | The request object ID. | `string` |
| `application` | App associated with the request. | [`App`](https://developers.facebook.com/docs/graph-api/reference/app/) |
| `to` | The recipient of the request. | [`User`](https://developers.facebook.com/docs/graph-api/reference/user/) |
| `from` | The sender associated with the request. This is only included for [user to user requests](https://developers.facebook.com/docs/howtos/requests#user_to_user). | [`User`](https://developers.facebook.com/docs/graph-api/reference/user/) |
| `message` | A string describing the request. | `string` |
| `created_time` | Timestamp when the request was created. | `datetime` |