platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query

### Adding a query to your request

To add your query to your request, you must use the query parameter. As with any query parameters, you must make sure to HTTP encode the query that you developed.

Here is an example of what this might look like using a cURL command, with an additional tweet.fields and max\_results parameter included. If you would like to use this command, please make sure to replace $BEARER\_TOKEN with your own [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0):

      `curl https://api.twitter.com/2/tweets/search/recent?query=cat%20has%3Amedia%20-grumpy&tweet.fields=created_at&max_results=100 -H "Authorization: Bearer $BEARER_TOKEN"`