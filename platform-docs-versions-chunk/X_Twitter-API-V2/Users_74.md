platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/follows/migrate/manage-follows-standard-to-twitter-api-v2


### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * POST https://api.twitter.com/1.1/friendships/create.json  
        (follow a user)
    * POST https://api.twitter.com/1.1/friendships/destroy.json  
        (unfollow a user)
* Twitter API v2 endpoint:
    * POST https://api.twitter.com/2/users/:id/following  
        (follow a user)
    * DELETE https://api.twitter.com/2/users/:source\_user\_id/following/:target\_user\_id  
        (unfollow a user) 

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated to a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.  
  

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

| Standard v1.1 | Twitter API v2 |
| --- | --- |
| No equivalent | id (POST), source\_user\_id (DELETE) |
| user\_id | target\_user\_id |
| screen\_name | No equivalent |

Please note that the Standard v1.1 parameters are passed as query parameters, whereas the Twitter API v2 parameters are passed as body parameters (for the POST endpoint) or path parameters (for the DELETE endpoint).

Also, the v2 id and source\_user\_id are not required when using the standard v1.1 endpoints since the Access Tokens passed with OAuth 1.0a User Context inferred which user was initiating the follow/unfollow.