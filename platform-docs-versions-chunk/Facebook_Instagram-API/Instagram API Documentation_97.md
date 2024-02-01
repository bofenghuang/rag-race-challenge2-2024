platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/webhooks

### Endpoint Requirements

* the app user's Page Access Token
* [pages\_manage\_metadata](https://developers.facebook.com/docs/instagram-api/guides/docs/permissions/reference/pages_manage_metadata)

#### Request Syntax

POST /{page\-id}/subscribed\_apps
  ?access\_token\={access\-token}
  &subscribed\_fields\={fields}

#### Request Parameters

| Value Placeholder | Value Description |
| --- | --- |
| `{page_id}` | ID of the Page connected to the app user's account. |
| `{access_token}` | App user's Page access tToken. |
| `{fields}` | A Page field (example: `feed`). |

Your app does not receive notifications for changes to a field unless you configure Page subscriptions in the App Dashboard and subscribe to that field.

#### Sample Request

curl \-i \-X POST \\
  "https://graph.facebook.com/`v19.0`/1755847768034402/subscribed\_apps?subscribed\_fields=feed&access\_token=EAAFB..."

##### Sample Response

{
  "success": true
}

[](#)

## Common Uses