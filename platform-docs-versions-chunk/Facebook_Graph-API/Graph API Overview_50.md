platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### Error Codes

When your app reaches its Business Use Case rate limit, subsequent requests made by your app will fail and the API will respond with an error code.

| Error Code | BUC Rate Limit Type |
| --- | --- |
| `error code 80000, error subcode 2446079` | Ads Insights |
| `error code 80004, error subcode 2446079` | Ads Management |
| `error code 80003, error subcode 2446079` | Custom Audience |
| `error code 80002` | Instagram |
| `error code 80005` | LeadGen |
| `error code 80006` | Messenger |
| `error code 32` | Page calls made with a User access token |
| `error code 80001` | Page calls made with a Page or System User access token |
| `error code 17, error subcode 2446079` | V3.3 and Older Ads API excluding Ads Insights |
| `error code 80008` | WhatsApp Business Management API |
| `error code 80014` | Catalog Batch |
| `error code 80009` | Catalog Management |

#### SampleError Code Message

{   
"error": {      
    "message": "(#80001) There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting.",      
    "type": "OAuthException",      
    "code": 80001,      
    "fbtrace\_id": "AmFGcW\_3hwDB7qFbl\_QdebZ"   
    }
}