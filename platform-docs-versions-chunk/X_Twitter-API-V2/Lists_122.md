platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-members/migrate/manage-list-members-standard-to-twitter-api-v2


### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * POST https://api.twitter.com/1.1/lists/members/create.json  
        (Adds a member to a specified List)
    * POST https://api.twitter.com/1.1/lists/members/destroy.json  
        (Removes a member from a specified List)
* Twitter API v2 endpoint:
    * POST https://api.twitter.com/2/lists/:id/members  
        (Adds a member to a specified List)  
        
    * DELETE https://api.twitter.com/2/lists/:id/members/:user\_id  
        (Removes a member from a specified List)

#### Rate limits

| **Standard v1.1** | **Twitter API v2** |
| --- | --- |
| /1.1/lists/members/create.json<br><br>none | /2/lists/:id/members<br><br>300 requests per 15-minute window with OAuth 1.0a User Context<br><br>300 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE |
| /1.1/lists/members/destroy.json<br><br>none | /2/lists/:id/members/:user\_id<br><br>300 requests per 15-minute window with OAuth 1.0a User Context<br><br>300 requests per 15-minute window with OAuth 2.0 Authorization Code with PKCE |

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps related to a project.

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

| **Standard v1.1** | **Twitter API v2** |
| --- | --- |
| list\_id | id  |
| slug | No equivalent |
| screen\_name | No equivalent |
| owner\_screen\_name | No equivalent |
| owner\_id | No equivalent |