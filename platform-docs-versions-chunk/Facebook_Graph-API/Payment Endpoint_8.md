platform: Facebook
topic: Graph-API
subtopic: Payment Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Payment Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/payment/dispute

### Permissions

* An app access token is required to settle any disputes for that app.
    
* If the payment has not been disputed yet, the call will return an error.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `reason` | The reason you are settling this dispute. This is required. | `enum{GRANTED_REPLACEMENT_ITEM, DENIED_REFUND, BANNED_USER}` |

### Response

If successful:

{
  "success": true
}

Otherwise a relevant error message will be returned.

## Deleting

You can't delete using this edge.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)