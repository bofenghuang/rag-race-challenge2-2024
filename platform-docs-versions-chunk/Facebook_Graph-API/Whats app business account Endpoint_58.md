platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/phone_numbers/

### Parameters

| Parameter | Description |
| --- | --- |
| `cc`<br><br>string | Country dial code of the phone number (for example, `1`). |
| `migrate_phone_number`<br><br>boolean | Set to `true` to migrate a registered WhatsApp Business Phone Number from one WhatsApp Business Account to another. |
| `phone_number`<br><br>string | Phone number without the country code or plus symbol (`+`). |
| `preverified_id`<br><br>string | Preverified ID related to this phone number |
| `verified_name`<br><br>string | Name of the business as it appears in the WhatsApp app or WhatsApp Business app profile. |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

## Updating

You can't perform this operation on this endpoint.