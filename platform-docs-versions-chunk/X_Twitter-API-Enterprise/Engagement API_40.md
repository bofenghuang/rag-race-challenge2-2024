platform: X
topic: Twitter-API-Enterprise
subtopic: Engagement API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Engagement API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/api-reference/post-insights-engagement


## Error Messages [¶](#error-messages- "Permalink to this headline")

In various scenarios, the Engagement API will occur situation-specific error messages that your application should be equipped to deal with. The table below includes common examples of these error messages and how you should interpret them. Please note that in many cases the Engagement API will return partial results for available data with specific error messages as part of a 200 OK response with more information.

| Error Message | Description |
| --- | --- |
| `"errors":["Your account could not be authenticated. Reason: Access token not found"]` | An error in the authentication component of the request. The “Reason” should provide information that is helpful to troubleshoot the error. In cases where you are not able to resolve, please send the full error, including the “Reason”, to our support team. |
| `"errors":["1 Tweet ID(s) are unavailable"],"unavailable_tweet_ids": ["TWEET_IDS"]` | The Tweet ID or IDs you have requested are no longer available, usually indicating that they have been deleted or are no longer publicly available for another reason. |
| `"errors":["Impressions & engagements for tweets older than 90 days (*TIME_PERIOD*) are not supported"],"unsupported_for_impressions_engagements_tweet_ids":[*TWEET_IDS*]` | The Tweet ID or IDs you have requested specific to the /totals endpoint are not 90 days or newer and are thus not available for returning the impressions or engagements metrics. |
| `"errors":["Forbidden to access tweets: *TWEET_IDS*"]` | The Tweet ID or IDs you have requested are not available based on the authentication token you are using to retrieve data on behalf of a third party. |