platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/migrate/manage-retweets-standard-to-twitter-api-v2


### Differences

#### Endpoint URLs and HTTP methods

* Standard v1.1 endpoints:
    * https://api.twitter.com/1.1/statuses/retweet/:id.json  
        (Retweets a tweet. Returns the original Tweet with Retweet details embedded)
    * https://api.twitter.com/1.1/statuses/unretweet/:id.json  
        (Undo a Retweet. Returns the original Tweet with Retweet details embedded)
* Twitter API v2 endpoint:
    * https://api.twitter.com/2/tweets/:id/retweets  
        (Retweets a given Tweet)
    * https://api.twitter.com/2/users/:id/retweets/:source\_tweet\_id  
        (Undo a Retweet of a given Tweet) 

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated to a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a Project.  
  

#### Request parameters

The following standard v1.1 request parameters accepted two request query parameters (user\_id or screen\_name). The Twitter API v2 only accepts the numerical user ID, and it must be passed as part of the endpoint path.

| Standard v1.1 | Twitter API v2 |
| --- | --- |
| **id** | **id** |
| **includes\_entities** | No equivalent |

Please note that the Standard v1.1 parameters are passed as query parameters, whereas the Twitter API v2 parameters are passed as body parameters for the POST endpoint or path parameters for the DELETE endpoint.

Also, an id of the user Retweeting a Tweet is not required when using the standard v1.1 endpoints since the [Access Tokens](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) passed with [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) infer which user is initiating the Retweet/undoing a Retweet.