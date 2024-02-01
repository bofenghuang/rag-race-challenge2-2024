platform: X
topic: Twitter-API-V2
subtopic: Lists
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Lists.md
url: https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/quick-start


### Steps to build a List lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “List lookup”, and then choose "List by ID".  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do this with this endpoint, you must authenticate your request with either [App only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only), [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code), or [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) authentication methods.

For simplicity's sake, we are going to utilize App only with this request, but if you'd like to request private [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) or Lists, you will need to use one of the other authentication methods. 

To utilize App only, you must add your keys and tokens (specifically the [App only Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens)) to Postman by selecting the environment named “Twitter API v2” (in the top-right corner of Postman), and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

If you've done this correctly, these variables will automatically be pulled into the request's authorization tab.  
 

#### Step three: Identify and specify which List you would like to retrieve

You must specify a List that you would like to receive within the request. You can find the List ID by navigating to twitter.com and clicking on a List and then looking in the URL. For example, the following URL's List ID is 84839422.

https://twitter.com/i/lists/84839422

The target ID can be any valid List ID. In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the id path variable. Be sure not to include any spaces before or after any ID.

|     |     |
| --- | --- |
| **Key** | **Value** |
| id  | 84839422 (The List ID) |

  
Step four: Identify and specify which fields you would like to retrieve  

If you click the "Send" button after step three, you will receive the default [List object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/lists) fields in your response: id, name.

If you would like to receive additional fields, you will have to specify those fields in your request with list.fields and/or [expansion](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request three additional sets of fields from different objects:

* The additional created\_at field in the primary Lists object.
    
* The full [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) using the expansion parameter
    
* The additional user.created\_at field in the associated user object.
    

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| list.fields | created\_at | created\_at |
| expansions | owner\_id | includes.users.id,  <br>includes.users.name,  <br>includes.users.username |
| user.fields | created\_at | includes.users.created\_at |

You should now see a similar URL next to the “Send” button:

      `https://api.twitter.com/2/lists/84839422?list.fields=owner_id&expansions=owner_id&user.fields=created_at`
    

Step five: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": {     "id": "84839422",     "name": "Official Twitter Accounts",     "owner_id": "783214"   },   "includes": {     "users": [       {         "name": "Twitter",         "created_at": "2007-02-20T14:35:54.000Z",         "username": "Twitter",         "id": "783214"       }     ]   } }`