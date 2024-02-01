platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/likes/migrate/manage-likes-standard-to-twitter-api-v2


### Differences

#### Endpoint URLs and HTTP methods

* Standard v1.1 endpoints:
    * POST https://api.twitter.com/1.1/favorites/create.json  
        (like a Tweet)
    * POST https://api.twitter.com/1.1/favorites/destroy.json  
        (unlike a Tweet)
* Twitter API v2 endpoint:
    * POST https://api.twitter.com/2/tweets/:id/likes  
        (like a Tweet)
    * DELETE https://api.twitter.com/2/tweets/:id/likes/:tweet\_id  
        (unlike a Tweet) 

**Request limitations**

The v2 liked Tweets endpoint allows you to request 5 to 100 Tweets per request. You can use pagination tokens and multiple requests to get all of a user’s liked Tweets. The v1.1 GET favorites/list endpoint also allows you to pull all liked  Tweets, but you can pull from 20 to 200 Tweets per request.  

For the v2 liking users endpoint, you are limited to 100 liking users per Tweet.

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated to a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a Project.  
  

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

| Standard v1.1 | Twitter API v2 |
| --- | --- |
| id  | id  |
| includes\_entities | No equivalent |

Please note that the Standard v1.1 parameters are passed as query parameters, whereas the Twitter API v2 parameters are passed as body parameters for the POST endpoint or path parameters for the DELETE endpoint.

Also, an id of the user liking a Tweet is not required when using the standard v1.1 endpoints since the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) passed with [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) infer which user is initiating the like/unlike.