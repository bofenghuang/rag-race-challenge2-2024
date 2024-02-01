platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/product_appeal

### Response

An object indicating success or failure. Response does not indicate appeal outcome.

{
  "success": {success}
}

#### Response Contents

| Property | Value |
| --- | --- |
| `success` | Indicates if API accepted request (`true`) or did not accept request (`false`). Response does not indicate appeal outcome. |

### cURL Example

#### Request

curl -i -X POST \\
 "https://graph.facebook.com/`v19.0`/90010177253934/product\_appeal?appeal\_reason=product%20is%20a%20toy%20and%20not%20a%20real%20weapon&product\_id=4382881195057752&access\_token=EAAOc..."

#### Response

{
  "success": true
}

## Reading

**`GET /{ig-user-id}/product_appeal`**

Get appeal status of a rejected product.

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.