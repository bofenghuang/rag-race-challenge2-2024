platform: Facebook
topic: Graph-API
subtopic: Payment Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Payment Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/payment/refunds

### Permissions

* An app access token is required to issue any refunds for that app.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `currency` | The three-letter ISO code of the currency in which the refund amount is specified; it must be the same as the currency in which the original purchase was denominated. This is required. | `string` |
| `amount` | The amount to refund. This is required. It must be less than or equal to the `refundable_amount` field on the parent Payment object. | `string` |
| `reason` | The reason you are refunding this order. | `enum{MALICIOUS_FRAUD, FRIENDLY_FRAUD, CUSTOMER_SERVICE}` |

### Response

If successful:

{
  "success": true
}

Otherwise a relevant error message will be returned.