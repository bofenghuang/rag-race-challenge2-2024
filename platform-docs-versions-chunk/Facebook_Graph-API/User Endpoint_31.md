platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/user/ad_studies/

### Error Codes

| Error | Description |
| --- | --- |
| 270 | This Ads API request is not allowed for apps with development access level (Development access is by default for all apps, please request for upgrade). Make sure that the access token belongs to a user that is both admin of the app and admin of the ad account |
| 100 | Invalid parameter |

## Creating

You can make a POST request to `ad_studies` edge from the following paths:

* [`/{user_id}/ad_studies`](https://developers.facebook.com/docs/graph-api/reference/user/ad_studies/)

When posting to this edge, an [AdStudy](https://developers.facebook.com/docs/marketing-api/reference/ad-study/) will be created.