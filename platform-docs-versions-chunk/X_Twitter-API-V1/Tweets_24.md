platform: X
topic: Twitter-API-V1
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V1/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update

## Example Request[¶](#example-request "Permalink to this headline")

To obtain the generated oauth\_nonce, oauth\_token, and oauth\_signature you can use a REST tool such as Insomnia or Postman.

    curl -XPOST 
      --url 'https://api.twitter.com/1.1/statuses/update.json?status=hello' 
      --header 'authorization: OAuth
      oauth_consumer_key="oauth_customer_key",
      oauth_nonce="generated_oauth_nonce",
      oauth_signature="generated_oauth_signature",
      oauth_signature_method="HMAC-SHA1",
      oauth_timestamp="generated_timestamp",
      oauth_token="oauth_token",
      oauth_version="1.0"'

You many want to change the status from 'hello' to something different.

You can use also use any other OAuth helper library you'd like such as twurl.

    $ twurl -d 'status=Test tweet using the POST statuses/update endpoint' /1.1/statuses/update.json