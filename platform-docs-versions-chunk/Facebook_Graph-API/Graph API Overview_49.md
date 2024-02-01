platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### Headers

All API responses made by your app that are rate limited using the BUC logic include an `X-Business-Use-Case-Usage` (for v3.3 and older Ads API calls) HTTP header with a JSON-formatted string that describes current application rate limit usage. This header can return up to 32 objects in one call.

#### X-Business-Use-Case Usage Header Contents

| Error Code | Value Description |
| --- | --- |
| `business-id` | The ID of the business associated with the token making the API calls. |
| `call_count` | A whole number expressing the percentage of allowed calls made by your app over a rolling one hour period. |
| `estimated_time_to_regain_access` | Time, in minutes, until calls will not longer be throttled. |
| `total_cputime` | A whole number expressing the percentage of CPU time allotted for query processing. |
| `total_time` | A whole number expressing the percentage of total time allotted for query processing. |
| `type` | Type of rate limit applied. Value can be one of the following: `ads_insights`, `ads_management`, `custom_audience`, `instagram`, `leadgen`, `messenger`, or `pages`. |
| `ads_api_access_tier` | For `ads_insights` and `ads_management` types only. Tiers allows your app to access the Marketing API. By default, apps are in the `development_access` tier. `Standard_access` enables lower rate limiting. To get a higher rate limit and get to the standard tier, you can apply for the "Advanced Access" to the [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/overview/authorization#layer-2--access-levels--permissions--and-features) feature. |

#### Total CPU Time

The amount of CPU time the request takes to process. When total\_cputime reaches 100, calls may be throttled.

#### Total Time

The length of time the request takes to process. When total\_time reaches 100, calls may be throttled.

#### Ads API Access Tier

For `ads_insights` and `ads_management` types only. Tiers allows your app to access the Marketing API. By default, apps are in the `development_access` tier. `Standard_access` enables lower rate limiting. To get a higher rate limit and get to the standard tier, you can apply for the "Advanced Access" to the [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/overview/authorization#layer-2--access-levels--permissions--and-features) feature.

#### Sample X-Business-Use-Case-Usage Header Value

x-business-use-case-usage: {
    "{business-object-id}": \[
        {
            "type": "{rate-limit-type}",           //Type of BUC rate limit logic being applied.
            "call\_count": 100,                     //Percentage of calls made. 
            "total\_cputime": 25,                   //Percentage of the total CPU time that has been used.
            "total\_time": 25,                      //Percentage of the total time that has been used.   
            "estimated\_time\_to\_regain\_access": 19,  //Time in minutes to regain access.
            "ads\_api\_access\_tier": "standard\_access"  //Tiers allows your app to access the Marketing API. standard\_access enables lower rate limiting.
        }
    \],      
    "66782684": \[
        {
            "type": "ads\_management",
            "call\_count": 95,
            "total\_cputime": 20,
            "total\_time": 20,
            "estimated\_time\_to\_regain\_access": 0,
            "ads\_api\_access\_tier": "development\_access" 
        }
    \],
    "10153848260347724": \[
        {
            "type": "ads\_insights",
            "call\_count": 97,
            "total\_cputime": 23,
            "total\_time": 23,
            "estimated\_time\_to\_regain\_access": 0,
            "ads\_api\_access\_tier": "development\_access"
        }
    \],
    "10153848260347724": \[
        {
            "type": "pages",
            "call\_count": 97,
            "total\_cputime": 23,
            "total\_time": 23,
            "estimated\_time\_to\_regain\_access": 0
        }
    \],
...
}