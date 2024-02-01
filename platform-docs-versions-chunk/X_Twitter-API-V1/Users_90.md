platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-lookup

## Example Requests[¶](#example-requests "Permalink to this headline")

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/friendships/lookup.json?screen_name=andypiper%2Cbinary_aaron%2Ctwitterdev%2Chappycamper%2Charris_0ff' 
      --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
      oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
      oauth_token="access-token-for-authed-user", oauth_version="1.0"'

    $ twurl /1.1/friendships/lookup.json?screen_name=andypiper,binary_aaron,twitterdev,happycamper,harris_0ff