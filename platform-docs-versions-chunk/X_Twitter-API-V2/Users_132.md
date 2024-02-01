platform: X
topic: Twitter-API-V2
subtopic: Users
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Users.md
url: https://developer.twitter.com/en/docs/twitter-api/users/mutes/quick-start/mutes-lookup


### Steps to build a mutes lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

[Add Twitter API v2 to Postman](https://t.co/twitter-api-postman)

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Mutes” folder, and select “Mutes lookup”.  
 

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either [OAuth 1.0a User Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization Code with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  
 

#### Step three: Specify a user

With this endpoint, you must specify your user ID or the ID of an authenticated user to see who you or the authenticated user has muted.

  
In Postman, navigate to the "Params" tab and enter the authenticated user ID into the "Value" column of the id under “Path Variables” (at the bottom of the section), making sure to not include any spaces before or after ID.

Above the “Path Variables” section, you’ll notice there are optional “Query Params” to add. For this example, we will check the variable max\_results and add a value of 5.

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Parameter Type** |
| `id` | (your user ID) | Path |
| max\_results | 5   | Query |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default [user object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user) fields in your response: id, name, and username.

If you want to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the [fields](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields) and/or [expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions) parameters.

For this exercise, we will request three additional sets of fields from different objects:

1. The additional user.created\_at field in the primary user objects.
2. The associated pinned Tweets’ object’s default fields for the returned users: id and text.
3. The additional  tweet.created\_at field in the associated Tweet objects.

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| user.fields | created\_at | user.created\_at |
| expansions | pinned\_tweet\_id | tweet.id, tweet.text |
| tweet.fields | created\_at | includes.tweets.created\_at |

You should now see a similar URL with your own user ID instead of the example ID URL next to the "Send" button:

      `https://api.twitter.com/2/users/1324848235714736129/muting?user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=created_at&max_results=5`
    

#### Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

      `{   "data": [     {       "username": "TwitterDev",       "created_at": "2013-12-14T04:35:55.000Z",       "id": "2244994945",       "name": "Twitter Dev",       "pinned_tweet_id": "1430984356139470849"     }   ],   "includes": {     "tweets": [       {         "created_at": "2021-08-26T20:03:51.000Z",         "id": "1430984356139470849",         "text": "Help us build a better Twitter Developer Platform!\n \nTake the annual developer survey &gt;&gt;&gt; https://t.co/9yTbEKlJHH https://t.co/fYIwKPzqua"       }     ]   },   "meta": {     "result_count": 1   } }`
    

####   
Step six: Paginate through your results

You may notice that there is a meta object located at the bottom of the response. If you received a next\_token, this signals that there is another page of results that we can retrieve. To pull the next page of results, you will pull the value of the next\_token field and add it to the request as the value to an additional pagination\_token query parameter.  
 

|     |     |
| --- | --- |
| **Key** | **Value** |
| pagination\_token | 1710819323648428707 |

If you send the request after adding this additional parameter, the next five results will be delivered with the subsequent payload since we specified max\_results as 5 in step three. You can continue to repeat this process until all results have been returned, but you can also use the max\_results parameter to request up to 1000 users per request, so you don’t have to paginate through results quite as much.