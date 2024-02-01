platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### Error Codes

When an app or user has reached their rate limit, requests made by that app or user will fill and the API will respond with an error code.

#### Throttle Error Codes

  

| Error Code | Description |
| --- | --- |
| `4` | Indicates that the app whose token is being used in the request has reached its rate limit. |
| `17` | Indicates that the User whose token is being used in the request has reached their rate limit. |
| `17 with subcode 2446079` | Indicates that the token being used in the Ads API v3.3 or older request has reached its rate limit. |
| `32` | Indicates that the User or app whose token is being used in the Pages API request has reached its rate limit. |
| `613` | Indicates that a custom rate limit has been reached. To help resolving this issue, visit the supporting docs for the specific API you are calling for custom rate limits that may be applied. |
| `613 with subcode 1996` | Indicates that we have noticed inconsistent behavior in the API request volume of your app. If you have made any recent changes that affect the number of API requests, you may be encountering this error. |

#### Sample Response

{
  "error": {
    "message": "(#32) Page request limit reached",
    "type": "OAuthException",
    "code": 32,
    "fbtrace\_id": "Fz54k3GZrio"
  }
}