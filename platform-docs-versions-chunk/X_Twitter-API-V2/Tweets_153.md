platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/migrate/standard-to-twitter-api-v2


### cURL requests

#### The following section displays cURL requests for the standard v1.1 endpoint and its equivalent endpoint in v2.  

The requests are made using [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only). In order to run the following cURL requests, you will need to replace ACCESS\_TOKEN in the authorization header with your app access token. For v2 endpoints, your app access token must belong to a [developer App](https://developer.twitter.com/en/docs/apps/overview) within a [Project](https://developer.twitter.com/en/docs/projects/overview). 

The response payload returned by the v1.1 endpoint will be different from the response payload returned by the v2 endpoint. With v2, the response will include the default fields, as well as any other fields requested with the [fields](https://developer.twitter.com/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) parameters. You can use these parameters to request a different set of fields to be returned.  

**Standard v1.1 [GET search/tweets](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets) and v2 [GET tweets/search/recent](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent) endpoints**

      `curl --request GET \   --url 'https://api.twitter.com/1.1/search/tweets.json?q=from%3ATwitterDev%20-is%3Aretweet&count=100' \   --header 'Authorization: Bearer $ACCESS_TOKEN'`
    

      `curl --request GET \   --url 'https://api.twitter.com/2/tweets/search/recent?query=from%3ATwitterDev%20-is%3Aretweet&tweet.fields=created_at%2Cconversation_id%2Centities&max_results=100' \   --header 'Authorization: Bearer $ACCESS_TOKEN'`