platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/

### Parameters

| Parameter | Description |
| --- | --- |
| `verification_code`<br><br>string | The verification code which was sent to the WhatsApp number. |
| `whatsapp_number`<br><br>string | The WhatsApp number to be verified.<br><br>Required |

### Return Type

Struct {

`error_message`: string,

`verification_status`: enum,

`whatsapp_number_type`: int32,

`whatsapp_display_number`: string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

You can update a [Page](https://developers.facebook.com/docs/graph-api/reference/page/) by making a POST request to [`/{page_id}/assigned_users`](https://developers.facebook.com/docs/graph-api/reference/page/assigned_users/).