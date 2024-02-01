platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-unretweet-id

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numerical ID of the desired status. |     | _123_ |
| trim\_user | optional | When set to either _true_ , _t_ or _1_ , each Tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. |     | _true_ |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/statuses/unretweet/1050118621198921728.json`