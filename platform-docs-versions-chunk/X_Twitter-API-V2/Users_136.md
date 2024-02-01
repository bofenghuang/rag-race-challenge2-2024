platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/mutes/quick-start/manage-mutes-quick-start


### Steps to build a manage mutes request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Mutes” folder, and select “Mute a user’s ID”.  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Specify who is going to mute whom

Manage mutes endpoints require two IDs: one for the user (the user who wishes to mute or unmute another user) and the target user (the user that will be muted or unmuted). The user’s ID must correspond to the authenticating user’s ID, meaning that you must pass the Access Tokens associated with the user ID when authenticating your request. In this case, you can specify the ID belonging to your own user. You can find your ID in two ways:

1. Using the [user lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference) by username endpoint, you can pass a username and receive the id field. 
2. Looking at your Access Token, you will find that the numeric part is your user ID.  
     

The target ID can be any valid user ID. In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the `id` path variable. Navigate to the “Body” tab and ID of the user you wish to mute as the value for the target\_user\_id parameter. Be sure not to include any spaces before or after any ID.

|     |     |
| --- | --- |
| **Key** | **Value** |
| `id` | authenticated user ID |
| target\_user\_id | the user ID you wish to mute |

#### Step four: Make your request and review your response

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{ "data": { "muting": true } }`
    

If you receive a "muting": true, then the id is successfully muting the target\_user\_id

To unmute the same user you can use the request entitled “Unmute a user ID”, which is also found in the “Mutes” folder of the Twitter API v2 collection loaded in Postman. The source\_user\_id should be your user ID and target\_user\_id should be the user ID to unmute. You will not have to add this as a JSON body so you will want to make sure that you add in the requisite query params for source\_user\_id and target\_user\_id.

On a successful unmute, you will receive a similar response to the following example:

      `{ "data": { "muting": false } }`