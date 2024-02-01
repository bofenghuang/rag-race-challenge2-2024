platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-favorites-create

## Parameters[¶](#parameters "Permalink to this headline")

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numerical ID of the Tweet to like. |     | _123_ |
| include\_entities | optional | The _entities_ node will be omitted when set to _false_ . |     | _false_ |

## Example Request[¶](#example-request "Permalink to this headline")

    curl --request POST 
    --url 'https://api.twitter.com/1.1/favorites/create.json?id=TWEET_ID_TO_FAVORITE' 
    --header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
    --header 'content-type: application/json'

## Example Response[¶](#example-response "Permalink to this headline")

    {tweet-object,
    "user": {user-object}
    }