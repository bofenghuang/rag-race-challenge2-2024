platform: Facebook
topic: Instagram-API
subtopic: API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/API Reference.md
url: https://developers.facebook.com/docs/instagram-api/reference/ig-media/insights

### Breakdown

You can also specify one or more breakdowns, and the results will be broken down into smaller sets based on the specified breakdown. Values can be:

* `action_type` — Only compatible with the profile\_activity metric. Break down results by profile UI component that viewers tapped or clicked after viewing the app user's profile. Response values can be:
    * `BIO_LINK_CLICKED`
    * `CALL`
    * `DIRECTION`
    * `EMAIL`
    * `OTHER`
    * `TEXT`
* `story_navigation_action_type` — Break down results by navigation action taken by the viewer upon viewing the media.
    * `TAP_BACK`
    * `TAP_EXIT`
    * `TAP_FORWARD`
    * `SWIPE_FORWARD`

Refer to the [Metrics](#metrics) table to determine which metrics support breakdowns and which breakdowns they support. If you request a metric that doesn't support breakdowns, the API will return an error ("`An unknown error has occurred.`"), so be careful if requesting multiple metrics in a single query.