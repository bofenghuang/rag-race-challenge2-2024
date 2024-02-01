platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/overview

## Overview

The following API endpoints can be used to programmatically create, retrieve and delete Tweets, Retweets and Likes:

|     |     |     |
| --- | --- | --- |
| **Tweets** | **Retweets** | **Likes (formerly favorites)** |
| * POST statuses/update<br>* POST statuses/destroy/:id<br>* GET statuses/show/:id<br>* GET statuses/oembed<br>* GET statuses/lookup | * POST statuses/retweet/:id<br>* POST statuses/unretweet/:id<br>* GET statuses/retweets/:id<br>* GET statuses/retweets\_of\_me<br>* GET statuses/retweeters/ids | * POST favorites/create/:id<br>* POST favorites/destroy/:id<br>* GET favorites/list |

For more details, please see the individual endpoint information within the [API reference](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference) section.