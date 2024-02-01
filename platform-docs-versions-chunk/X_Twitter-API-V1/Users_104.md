platform: X
topic: Twitter-API-V1
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup

## Example Requests[¶](#example-requests "Permalink to this headline")

    $ curl --request GET 
      --url 'https://api.twitter.com/1.1/users/lookup.json?user_id=783214,6253282' 
      --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
      oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
      oauth_version="1.0"'

    $ twurl /1.1/users/lookup.json?user_id=783214,6253282,2244994945

## Example Response[¶](#example-response "Permalink to this headline")

    [
      {
        {user-object},
        {user-object},
        {user-object}
      }
    ]

For more detail, see the [user-object definition](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object).