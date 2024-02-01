platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### Headers

Endpoints that receive enough requests from your app will include a `X-App-Usage` or `X-Ad-Account-Usage` (for v3.3 and older Ads API calls) HTTP header in their responses. The header will contain a JSON-formatted string that describes current application rate limit usage.

#### Header Contents

  

| Key | Value Description |
| --- | --- |
| `call_count` | A whole number expressing the percentage of calls made by your app over a rolling one hour period. |
| `total_cputime` | A whole number expressing the percentage of CPU time allotted for query processing. |
| `total_time` | A whole number expressing the percentage of total time allotted for query processing. |

#### X-Ad-Account-Usage Header Contents

| Key | Value Description |
| --- | --- |
| `acc_id_util_pct` | The percentage of calls made for this ad account before the rate limit is reached. |
| `reset_time_duration` | Time duration (in seconds) it takes to reset the current rate limit to 0. |
| `ads_api_access_tier` | Tiers allows your app to access the Marketing API. By default, apps are in the `development_access` tier. `Standard_access` enables lower rate limiting. To get a higher rate limit and get to the standard tier, you can apply for the "Advanced Access" to the [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/overview/authorization#layer-2--access-levels--permissions--and-features) feature. |

#### Total CPU Time

The amount of CPU time the request takes to process. When `total_cputime` reaches 100, calls may be throttled.

#### Total Time

The length of time the request takes to process. When `total_time` reaches 100, calls may be throttled.

#### Sample X-App-Usage Header Value

x-app-usage: {
    "call\_count": 28,         //Percentage of calls made 
    "total\_time": 25,         //Percentage of total time
    "total\_cputime": 25       //Percentage of total CPU time
}

#### Sample X-Ad-Account-Usage Header Value

x-ad-account-usage: {
    "acc\_id\_util\_pct": 9.67,   //Percentage of calls made for this ad account.
    "reset\_time\_duration": 100,   //Time duration (in seconds) it takes to reset the current rate limit score.
    "ads\_api\_access\_tier": 'standard\_access'   //Tiers allows your app to access the Marketing API. standard\_access enables lower rate limiting.
}