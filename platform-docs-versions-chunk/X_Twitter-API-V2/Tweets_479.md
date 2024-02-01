platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/hide-replies/quick-start


## 

####   
Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Find a Tweet ID to hide

The hide replies endpoint can hide or unhide replies on behalf of an authorized user. Because we are using the Access Tokens related to your user profile in this example, you will be able to hide replies from users who participate in a conversation started by you. Similarly, if you were using Access Tokens that belong to another user that authorized your app, you would be able to moderate replies to any conversations started by that account.

Ask a friend to reply to a Tweet (let them know you're testing hide replies) or reply to any of your Tweets from a test account. Click on that reply, then copy the numeric part of its URL. That will be the Tweet ID we will hide.

In this case, we will be looking at the following Tweet, which has the ID `1232720193182412800`:

`https://twitter.com/TwitterDev/status/1232720193182412800`

####   
Step four: Hide the Tweet

In Postman, open the Hide replies folder and select Hide a reply. In the Params tab, paste the Tweet ID next to the id field (you won't need to replace :id in the URL). Click "Send" and you will see a successful response.

      `{"hidden":true}`
    

#### Step five: Unhide the Tweet  

Hidden Tweets are moved to a separate tab in the Twitter app. To unhide a tweet in Postman, open the Hide replies folder and select Unhide a reply. In the Params tab, paste the same Tweet ID used in the previous step next into the id field. Click "Send" and you will see a successful response.

      `{"hidden":false}`
    

  
The hidden field represents the hidden status of the Tweet. A hidden status of true means the Tweet is hidden. Similarly, false means the Tweet is not hidden.