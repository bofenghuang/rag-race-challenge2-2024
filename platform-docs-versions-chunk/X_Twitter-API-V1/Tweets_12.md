platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets

## Example Requests[¶](#example-requests "Permalink to this headline")

    $ curl --request GET 
     --url 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular' 
     --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
     oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
     oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
     oauth_token="access-token-for-authed-user", oauth_version="1.0"'

    $ twurl /1.1/search/tweets.json?q=nasa&result_type=popular