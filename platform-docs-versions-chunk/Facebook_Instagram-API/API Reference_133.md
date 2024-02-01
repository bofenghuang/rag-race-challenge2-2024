platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-user/insights


### Breakdown

If you request `metric_type=total_value`, you can also specify one or more breakdowns, and the results will be broken down into smaller sets based on the specified breakdown. Values can be:

* `contact_button_type` — Break down results by profile UI component that viewers tapped or clicked. Response values can be:
    * `BOOK_NOW`
    * `CALL`
    * `DIRECTION`
    * `EMAIL`
    * `INSTANT_EXPERIENCE`
    * `TEXT`
    * `UNDEFINED`
* `follow_type` — Break down results by followers or non-followers. Response values can be:
    * `FOLLOWER`
    * `NON_FOLLOWER`
    * `UNKNOWN`
* `media_product_type` — Break down results by the surface where viewers viewed or interacted with the app user's media. Response values can be:
    * `AD`
    * `FEED`
    * `REELS`
    * `STORY`

Refer to the [Metrics](#metrics) table to determine which metrics are compatible with a breakdown. If you request a metric that doesn't support a breakdown, the API will return an error (`"An unknown error has occurred."`), so be careful if requesting multiple metrics in a single query.

If you request `metric_type=time_series`, breakdowns will not be included in the response.