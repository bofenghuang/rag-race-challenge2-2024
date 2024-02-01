platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/migrate/standard-to-twitter-api-v2


### cURL requests

#### The following section displays cURL requests for the standard v1.1 endpoints and their equivalent endpoints in v2.  

The requests are made using [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only). In order to run the following cURL requests, you will need to replace ACCESS\_TOKEN in the authorization header with your app access token. For v2 endpoints, your app access token must belong to a [developer App](https://developer.twitter.com/en/docs/apps/overview) within a [Project](https://developer.twitter.com/en/docs/projects/overview). 

The response payloads returned by v1.1 endpoints will be different from the response payloads returned by v2 endpoints. With v2, responses will include the default fields, as well as any other fields requested with the [fields](https://developer.twitter.com/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) parameters. You can use these parameters to request a different set of fields to be returned.  

**Standard v1.1 [GET statuses/lookup](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-lookup) and v2 [GET /tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets) endpoints**

      `curl --request GET \   --url 'https://api.twitter.com/1.1/statuses/lookup.json?id=1460323737035677698%2C1460323743339741184' \   --header 'Authorization: Bearer $ACCESS_TOKEN'` 
    

      `curl --request GET \   --url 'https://api.twitter.com/2/tweets?ids=1460323737035677698%2C1460323743339741184&tweet.fields=created_at&expansions=author_id&user.fields=created_at' \   --header 'Authorization: Bearer $ACCESS_TOKEN'`
    

**Standard v1.1 [GET statuses/show/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-show-id) and v2 [GET /tweets/:id](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets-id) endpoints**

      `curl --request GET \   --url 'https://api.twitter.com/1.1/statuses/show.json?id=1460323737035677698' \   --header 'Authorization: Bearer $ACCESS_TOKEN'`
    

      `curl --request GET \   --url 'https://api.twitter.com/2/tweets/1460323737035677698?tweet.fields=created_at&expansions=author_id&user.fields=created_at' \   --header 'Authorization: Bearer $ACCESS_TOKEN'`