platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/migrate/list-lookup-standard-to-twitter-api-v2


### Differences

#### Endpoint URLs

* Standard v1.1 endpoints:
    * GET https://api.twitter.com/1.1/lists/show.json  
        (Lookup a specified List)
    * GET https://api.twitter.com/1.1/lists/ownerships.json  
        (Lookup specified user owned Lists)
* Twitter API v2 endpoint:
    * GET https://api.twitter.com/2/lists/:id  
        (Lookup a specified List)  
        
    * GET https://api.twitter.com/2/users/:id/owned\_lists  
        (Lookup specified user owned Lists)

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a [developer App](https://developer.twitter.com/en/docs/apps) that is associated with a [Project](https://developer.twitter.com/en/docs/projects) when authenticating your requests. All Twitter API v1.1 endpoints can use credentials from standalone Apps or Apps associated with a project.

####   
  
Data objects per request limits

The standard v1.1 /lists/ownerships endpoint allows you to return up to 1000 Lists per request. The new v2 endpoints allow you to return up to 100 Lists per request. By default, 100 user objects will be returned, to change the number of results you will need to pass a query parameter max\_results= with a number between 1-100; you can then pass the next\_token returned in the response payload to the pagination\_token query parameter in your next request.

**Response data format**

One of the biggest differences between standard v1.1 and Twitter API v2 endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by default and then have the option to use parameters to identify which additional fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the List id and name fields by default. To request any additional fields or objects, you will need to use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/fields) and [expansions](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/expansions) parameters. Any List fields that you request from this endpoint will return in the primary List object. Any expanded Tweet or user object and fields will return an includes object within your response. You can then match any expanded objects back to the List object by matching the IDs located in both the user and the expanded Tweet object. 

Here are examples of possible List fields and expansions:

* created\_at
    
* follower\_count
    
* member\_count
    
* owner\_id
    
* description
    
* private
    

|     |     |
| --- | --- |
| **Endpoint** | **Expansion** |
| /2/lists/:id | owner\_id |
| /2/users/:id/owned\_lists | owner\_id |

We encourage you to read more about these new parameters in their respective guides, or by reading our guide on [how to use fields and expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions). 

We have also put together a [data format migration guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2) that can help you map standard v1.1 fields to the newer v2 fields. This guide will also provide you with the specific expansion and field parameter that you will need to pass with your v2 request to return specific fields. 

In addition to the changes in how you request certain fields, Twitter API v2 is also introducing new JSON designs for the objects returned by the APIs, including [Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) and [user](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) objects.

* At the JSON root level, the standard endpoints return Tweet objects in a statuses array, while Twitter API v2 returns a data array. 
    
* Instead of referring to Retweeted and Quoted "statuses", Twitter API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and deprecated fields, such as contributors and user.translator\_type are being removed. 
    
* Instead of using both favorites (in Tweet object) and favourites (in user object), Twitter API v2 uses the term like. 
    
* Twitter is adopting the convention that JSON values with no value (for example, null) are not written to the payload. Tweet and user attributes are only included if they have non-null values.  
     
    

#### Request parameters

The following standard v1.1 request parameters have equivalents in Twitter API v2:

**List lookup by ID**

|     |     |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| list\_id | id  |
| slug | No equivalent |
| owner\_screen\_name | No equivalent |
| owner\_id | Requested with expansions/fields parameter |

**User owned List lookup**

|     |     |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| user\_id | id  |
| screen\_name | No equivalent |
| count | max\_results |
| cursor | pagination\_token |
|     |     |