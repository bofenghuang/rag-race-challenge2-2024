platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update

## Resource URL[¶](#resource-url "Permalink to this headline")

`https://api.twitter.com/1.1/statuses/update.json`

## Resource Information[¶](#resource-information "Permalink to this headline")

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 3-hour window | 300\* per user; 300\* per app |

_Please note_ - The 300 per 3 hours is a combined limit with the [POST statuses/retweet/:id](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-retweet-id) endpoint. You can only post 300 Tweets or Retweets during a 3 hour period.