platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-destroy

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| screen\_name | optional | The screen name of the user to unfollow. |     | _twitterdev_ |
| user\_id | optional | The ID of the user to unfollow. |     | _2244994945_ |

## Example Request[¶](#example-request "Permalink to this headline")

`POST https://api.twitter.com/1.1/friendships/destroy.json?user_id=2244994945`

## Example Response[¶](#example-response "Permalink to this headline")

    {user-object,
      "status": {tweet-object}
    }

For more detail, see the [user-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object) and the [tweet-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object).