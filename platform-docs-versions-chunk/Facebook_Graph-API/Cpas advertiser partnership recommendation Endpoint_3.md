platform: Facebook
topic: Graph-API
subtopic: Cpas advertiser partnership recommendation Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Cpas advertiser partnership recommendation Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/cpas-advertiser-partnership-recommendation/

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | ID of the recommendation object. |
| `advertiser_business_id`<br><br>numeric string | Recommended advertiser for this partnership. |
| `brand_business_id`<br><br>numeric string | Recommended brand for this partnership. |
| `brands`<br><br>list<string> | Brands that can be advertised for in this partnership. |
| `countries`<br><br>list<string> | Countries in which the partnership could run ads. |
| `merchant_business_id`<br><br>numeric string | Recommended retailer for this partnership. |
| `merchant_categories`<br><br>list<string> | Categories associated with the retailer's products. |
| `status`<br><br>enum | Current status of this recommendation based on actions taken on it. |
| `status_reason`<br><br>enum | Reason why this recommendation has its current status. |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |