platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/batch-requests

### Limitations

* Batch requests are limited to 50 requests per batch. Each call within the batch is counted separately for the purposes of calculating API call limits and resource limits. For example, a batch of 10 API calls will count as 10 calls and each call within the batch contributes to CPU resource limits in the same manner. Please see our [Rate Limiting Guide](https://developers.facebook.com/docs/graph-api/overview/rate-limiting) for more information.
* Batch requests cannot include multiple [Adsets](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign) under the same [Campaign](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group). Learn more about [batching Marketing API requests](https://developers.facebook.com/docs/marketing-api/asyncrequests).