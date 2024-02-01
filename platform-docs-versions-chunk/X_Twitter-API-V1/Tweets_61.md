platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweeters-ids

GET statuses/retweeters/ids

get-statuses-retweeters-ids

# GET statuses/retweeters/ids

Returns a collection of up to 100 user IDs belonging to users who have retweeted the Tweet specified by the `id` parameter.

This method offers similar data to [GET statuses / retweets / :id](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-retweets-id).

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/statuses/retweeters/ids.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 15-min window (app auth) | 300 |