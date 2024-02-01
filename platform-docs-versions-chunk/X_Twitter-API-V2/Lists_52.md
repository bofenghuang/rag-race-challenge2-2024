platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/migrate/manage-lists--standard-v1-1-compared-to-twitter-api-v2


### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * POST https://api.twitter.com/1.1/lists/create.json  
        (Creates a List)
    * POST https://api.twitter.com/1.1/lists/destroy.json  
        (Deletes a List)
    * POST https://api.twitter.com/1.1/lists/update.json  
        (Updates a List)
* Twitter API v2 endpoint:
    * POST https://api.twitter.com/2/lists  
        (Creates a List)  
        
    * DELETE https://api.twitter.com/2/lists/:id  
        (Deletes a List)  
        
    * PUT https://api.twitter.com/2/lists/:id  
        (Updates a List)  
          
        

#### Rate limits

| **Standard v1.1** | **Twitter API v2** |
| --- | --- |
| /1.1/lists/create.json<br><br>none | /2/lists<br><br>300 requests per 15-minute window with OAuth 1.0a User Context |
| /1.1/lists/destroy.json<br><br>none | /2/lists/:id<br><br>300 requests per 15-minute window with OAuth 1.0a User Context |
| /1.1/lists/update.json<br><br>none | /2/lists/:id<br><br>300 requests per 15-minute window with OAuth 1.0a User Context |

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) associated with a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps related to a project.

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

**Create a List**  

| **Standard** | **Twitter API v2** |
| --- | --- |
| name | name |
| mode | private |
| description | description |

**Delete/Update a List**

| **Standard** | **Twitter API v2** |
| --- | --- |
| owner\_screen\_name | No equivalent |
| owner\_id | No equivalent |
| list\_id | id  |
| slug | No equivalent |

**Please note:** Standard v1.1 parameters are passed as query parameters, whereas the Twitter API v2 parameters are passed as body parameters (for the POST endpoint) or path parameters (for the DELETE and PUT endpoints).