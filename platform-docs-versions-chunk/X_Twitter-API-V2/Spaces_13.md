platform: X
topic: Twitter-API-V2
subtopic: Spaces
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Spaces.md
url: https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/quick-start


### Steps to build a Spaces lookup request

_For this example, we will make a request to the user Spaces lookup by creator ID endpoint, but you can apply the learnings from this quick start to other lookup requests as well._ 

**Step one: Start with a tool or library**

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the Spaces folder and find the "Lookup Spaces created by one or more users" request.  
 

**Step two: Authenticate your request**

To properly make a request to the Twitter API, you need to verify that you have permission. To do so, this endpoint requires you to authenticate your request with either [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) authentication methods.

For simplicity's sake, we will utilize OAuth 2.0 App-Only with this request, but you will need to use one of the other authentication methods if you'd like to request private [metrics](https://developer.twitter.com/en/docs/twitter-api/metrics) or Spaces from a private user. 

To utilize OAuth 2.0 App-Only, you must add your keys and tokens, specifically the [App Access Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) (also known as the App-only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

**Step three: Identify and specify which user from which you would like to retrieve Tweets**

You must specify a user you would like to retrieve live or upcoming Spaces for within the request. In this example, we will be passing a single user ID.

User IDs are simply the numerical value that represents an account handle that you can find within an account's profile URL. For example, the following account’s username is TwitterDev.

https://twitter.com/TwitterDev

To convert this username to the user ID, you will have to use the user lookup endpoint with the username and find the numerical user ID in the payload. In the case of @TwitterDev, the user ID is 2244994945.

In Postman, navigate to the "Params" tab and enter this user ID into the "Value" column of the id parameter.

|     |     |
| --- | --- |
| **Key** | **Value** |
| id  | 2244994945 |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive an id, which is the only [Space object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space) field returned by default in your response.

If you would like to receive additional fields, you will have to specify them in your request with the space.fields or expansions parameters.

For this exercise, we will requested three additional sets of fields from different objects:

* The additional title field in the primary Spaces object.
* The full [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) of the specified creator ID
* The additional user.created\_at field in the associated user object.

In Postman, navigate to the “Params” tab and add the following key:value pair to the “Query Params” table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| space.fields | title | creator\_id |
| expansions | creator\_id | includes.users.id, includes.users.name, includes.users.username |
| user.fields | created\_at | includes.users.created\_at |

You should now see the following URL next to the “Send” button:

https://api.twitter.com/2/spaces/by/creator\_ids?user\_ids=2244994945&space.fields=creator\_id&expansions=creator\_id&user.fields=created\_at

**  
Step five: Make your request and review your response**

Once you have everything set up, hit the “Send” button and you will receive the following response:

      `{    "data": [     {         "creator_id": "2244994945",         "id": "1zqKVXPQhvZJB",         "title": "Hello world 👋",         "state": "Running"    },    "includes": {        "users": [            {                "created_at": "2013-12-14T04:35:55.000Z",                "name": "Twitter Dev",                "id": "2244994945",                "username": "TwitterDev"            }        ]    } ] }`