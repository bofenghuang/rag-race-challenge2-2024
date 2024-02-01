platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/follows/quick-start/manage-follows


### Steps to build a manage follows request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Follows” folder, and select “Follow a user ID”.  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Specify who is going to follow whom

Manage follows endpoints take two IDs: one for the source user (the user who wishes to follow or unfollow another user) and the target user (the user that will be followed or unfollowed). The source user’s ID must correspond to the user ID of the authenticating user. In this case, you can specify the ID belonging to your own user. You can find your ID in two ways:

1. Using the [user lookup by username](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference) endpoint, you can pass a username and receive the id field. 
2. Looking at your Access Token, you will find that the numeric part is your user ID.  
     

The target ID can be any valid user ID. For example the user ID for @TwitterDev is 2244994945.

In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the id path variable. Navigate to the “Body” tab and and 2244994945 (the user ID for @TwitterDev) as the value for the target\_user\_id parameter. Making sure to not include any spaces before or after any ID.

|     |     |
| --- | --- |
| **Key** | **Value** |
| `id` | (your user ID) |
| target\_user\_id | 2244994945 |

  
If you click the "Send" button, you will receive a response object containing the status of the relationship:

* If you receive a "following": true, then the id is successfully following the target\_user\_id.
* If you receive a "pending": true, then the target\_user\_id is protected and must accept your follow request.

####   
Step four: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive the following response:

      `{     "data": {         "following": true,         "pending_follow": false     } }`
    

Similarly, if you were trying to unfollow a user, you would use the "Unfollow a user ID" request within the same Postman collection. However, both the source\_user\_id and target\_user\_id parameters should be passed as path variables using the unfollow endpoint.