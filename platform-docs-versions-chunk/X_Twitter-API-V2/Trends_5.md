platform: X
topic: Twitter-API-V2
subtopic: Trends
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Trends.md
url: https://developer.twitter.com/en/docs/twitter-api/trends/api-reference/get-trends-by-woeid

GET /2/trends/by/woeid/:woeid

# GET /2/trends/by/woeid/:woeid

Get the trends for a location

### Endpoint URL

`https://api.twitter.com/2/trends/by/woeid/:woeid`  
  

### Authentication and rate limits

|     |     |
| --- | --- |
| Authentication methods  <br>supported by this endpoint | [OAuth 2.0 App-only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only "Use this method to obtain information in the context of an unauthenticated public user. This method is for developers that just need read-only access to public information. Click to learn how to obtain an OAuth 2.0 App Access Token.") |
| [Rate limit](https://developer.twitter.com/en/docs/rate-limits) | App rate limit (Application-only): 75 requests per 15-minute window shared among all users of your app |

### Path parameters

| Name | Type | Description |
| --- | --- | --- |
| `woeid`  <br> Required | number | The where-on-earth ID (woeid) for a location |