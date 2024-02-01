platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/migrate/manage-tweets-standard-to-twitter-api-v2


### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * https://api.twitter.com/1.1/statuses/update.json  
        (Creates a Tweet)
    * `https://api.twitter.com/1.1/statuses/destroy/:id.json`  
        (Deletes a Tweet)
* Twitter API v2 endpoint:
    * https://api.twitter.com/2/tweets  
        (Creates a Tweet)
    * https://api.twitter.com/2/tweets/:id  
        (Deletes a specified Tweet)

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/content/developer-twitter/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/content/developer-twitter/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.

#### Request parameters

The following standard v1.1 request parameters accepted two request query parameters (user\_id or screen\_name). The Twitter API v2 only accepts the numerical Tweet ID for the DELETE endpoint, and it must be passed as part of the endpoint path.

For the POST endpoint, additional parameters will need to be passed in via the JSON body of the request. You can learn more about what parameters are available in the [API reference guide](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference).