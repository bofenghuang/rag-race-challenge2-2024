platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/product_appeal

### Response

A JSON-formatted object containing an array of appeal status metadata.

{
  "data": \[
    {
      "eligible\_for\_appeal": {eligible-for-appeal},
      "product\_id": {product-id},
      "review\_status": "{review-status}"
    }
  \]
}

#### Response Contents

| Property | Value |
| --- | --- |
| `eligible_for_appeal` | Indicates if decision can be appealed (yes if `true`, no if `false`). |
| `product_id` | Product ID. |
| `review_status` | Review status. Value can be:<br><br>  <br><br>* `approved` — Product is approved.<br>* `rejected` — Product was rejected<br>* `pending` — Still undergoing review.<br>* `outdated` — Product was approved but has been edited and requires reapproval.<br>* `""` — No review status.<br>* `no_review` — No review status. |