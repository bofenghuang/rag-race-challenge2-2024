platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/quick-start


### Steps to building Direct Message lookup requests

In this example, in one request, we'll create a new group conversation and add our first message to it. We'll then add a second message to the created conversation.

#### Step one: Start with a tool or library

To begin working with the manage Direct Message endpoints we are going to use the Postman tool to simplify the process. A TwitterDev-authored collection of example Twitter API v2 requests will be used to explore six endpoints used to create new Direct Messages and to list Direct Message conversation events.

While most of the collection is pre-filled, there are a few details that you'll need to provide that are based on the Twitter App created to host these API requests. First, let's get the collection loaded/updated.

To load Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

  
  
Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Manage Direct Messages” folder. This folder's Authorization tab has been pre-filled where possible. You will need to update a few settings to share your Twitter App's authentication details.

This folder also contains three endpoints for creating new Direct Messages. Note that there is also a "Direct Message lookup" folder with three available endpoints for retrieving Direct Message conversation events, including sending and receiving messages, and when conversation participants join and leave.

Since creating group conversations is a new feature of the Twitter API v2, this example will focus on that. We will be working with the "New group DM and conversation" example. We will use this request to create a Direct Message group conversation.

The next step is to authenticate with the endpoint.

####   
Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission to do so. To make a successful request to this endpoint, we will be using [OAuth 2.0 Authorization Code Flow with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code). You can generate an access token within Postman. 

With Postman you can set the authentication method at the folder level or at the request level. Here we will be configuring the authentication details at the folder level. Navigate to the "Mange Direct Messages" folder, select the "Authorization" tab and confirm that the Type to set to “OAuth 2.0”, and "Add auth data to" is set to "Request Headers." In the "Current Token" section, make sure the "header Prefix" is set to Bearer.  

To configure and generate a new token:

1. Create a Token Name, such as "DM lookup."
    
2. Confirm that **Grant Type** is set to Authorization Code (with PKCE).
    
3. Set your **Callback URL**. You will want to update your Callback URL to exactly match the Callback URL associated with your application in the [v2 Dev Portal](https://developer.twitter.com/en/portal/dashboard). With the Twitter App used with this example, the Callback URL is set to - [https://www.example.com.](https://www.example.com/) (Note that since this must match exactly, [https://example.com](https://example.com/) would not work.) 
    
4. Confirm that **Auth URL** is set to [https://twitter.com/i/oauth2/authorize](https://twitter.com/i/oauth2/authorize)
    
5. Confirm that **Access Token URL** is set to [https://api.twitter.com/2/oauth2/token.](https://api.twitter.com/2/oauth2/token)**Client ID** \- Copy and paste OAuth 2.0 client ID from the Developer Portal  
    **Client Secret** - You will need this only if you are using an App type that is a confidential client. If so, copy and paste the OAuth 2.0 Client Secret from the Developer Portal. 
    
6. Confirm that **Scope** is set to dm.read dm.write tweet.read users.read.
    
7. Confirm that **State** is set to “state.”
    
8. Confirm that **Client Authentication** is set to Send as Basic Auth header.
    
9. Click where it says “Get New Access Token”, click "Authorize app" as part of the "Sign-in with Twitter" process.
    
10. Click the "Proceed" button and then the "Use Token" to generate a token. 
    
11. Click on the "Save" button to save these configuration details.
    

You may get a message that you are not logged into Twitter. If you get this error, you will need to log in to the Twitter account that you are trying to post on behalf of inside of Postman.

Now that these OAuth 2.0 details have been set at the folder level, navigate to each of the examples and their "Authorization" tab and confirm that they have their Type set to "Inherit auth from parent." 

Note that this token will expire soon, and you'll need to regenerate it by clicking on the "Get New Access Token" button. Clicking that will trigger the "Sign-in with Twitter" process and generate a fresh token to make requests with.

#### Step three: Retrieve Direct Messages conversation events

When retrieving Direct Message conversation events with this endpoint, you need to specify a conversation ID. The conversation ID is part of the endpoint path: https://api.twitter.com/2/dm\_conversations/:dm\_conversation\_id/dm\_events

In Postman, navigate to the “Params” tab and enter the ID of the conversation you want to retrieve events for in the "Path Variables" section.

The setting would be:

|     |     |
| --- | --- |
| **Key** | **Value** |
| `dm_conversation_id` | `1228393702244134912` |

With this conversation specified, the resulting path becomes https://api.twitter.com/2/dm\_conversations/1582103724607971328/dm\_events

If you click the "Send" button you will receive the default Direct Message object fields in your response: id,  text, and event\_type. There will also be a "meta" object with the number of results, along with pagination tokens used for retrieving more events if available.

      `{    "data": [        {            "event_type": "MessageCreate",            "id": "1580705921830768647",            "text": "hello to you two, this is a new group conversation."        }    ],    "meta": {        "result_count": 1,        "next_token": "18LAA5FFPEKJA52G0G00ZZZZ",        "previous_token": "1BLC45FFPEKJA52G0S00ZZZZ"    } }`
    

If you would like to receive additional fields, you will have to specify those fields in your request with the [field](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/fields) and/or [expansion](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/expansions) parameters.

For this exercise, we will request additional sets of fields of the dm\_event object:  

1. The default Direct Message object fields, id, text, and event\_type.
    
2. Additional Direct Message object fields: dm\_conversation\_id, created\_at, sender\_id, attachments, participant\_ids, referenced\_tweets
    

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |
| --- | --- |
| Key | Value |
| dm\_event.fields | dm\_conversation\_id,created\_at,sender\_id,attachments,participant\_ids,referenced\_tweets |

|     |     |     |
| --- | --- | --- |
|     |     |     |
|     |     |     |

You should now see the following URL next to the "Send" button:

https://api.twitter.com/2/dm\_conversations/:dm\_conversation\_id/dm\_events?dm\_event.fields=id,text,event\_type,dm\_conversation\_id,created\_at,sender\_id,attachments,participant\_ids,referenced\_tweets

#### Step four: Make your request and review your response

Once you have everything set up, hit the "Send" button again, and you will receive a response similar to the below response. Note that this response includes all the available dm\_event fields.

      `{    "data": [        {            "text": "hello to you two, this is a new group conversation.",            "id": "1580705921830768647",            "dm_conversation_id": "1580705921830768643",            "event_type": "MessageCreate",            "sender_id": "17200003",            "created_at": "2022-10-13T23:43:54.000Z"        }    ],    "meta": {        "result_count": 1,        "next_token": "18LAA5FFPEKJA52G0G00ZZZZ",        "previous_token": "1BLC45FFPEKJA52G0S00ZZZZ"    } }`