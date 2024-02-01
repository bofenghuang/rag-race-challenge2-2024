platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/volume-streams/quick-start/sampled-stream


### Steps to build a sampled stream request

#### Step one: Start with a cURL command

In this quick start, we are going to use a simple cURL request to connect a real-time stream to Twitter that will deliver 1% of all publicly available Tweets. The sampled stream endpoint is a very simple one. All you will have to do is replace or add a couple of elements of the below request and submit it to your command line tool.

      `curl -X GET "https://api.twitter.com/2/tweets/sample/stream" \ -H "Authorization: Bearer $APP_ACCESS_TOKEN"` 
    

#### Step two: Authenticate your request  

Since sampled stream requires [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) authentication, you will need to replace $APP\_ACCESS\_TOKEN with the App Access Token that you generated in the prerequisites.   
 

#### Step three: Identify and specify which fields you would like to retrieve

If you connect to the stream after step two, you will receive the default [Tweet object](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/object-reference/tweet) fields in your response: id , text, and edit\_history\_tweet\_ids. 

If you would like to receive additional fields beyond these default fields, you will have to specify those fields in your request with the [field](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/fields) and/or [expansion](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/expansions) parameters.  

For this exercise, we will request a three different sets of fields from different objects:

1. The additional tweet.created\_at field in the primary Tweet objects.
2. The associated authors’ user object’s default fields for the returned Tweets: id, name, username
3. The additional  user.created\_at field in the associated user objects.   
     

To request these fields, you will need to pass the following in your request:  
 

|     |     |     |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| `tweet.fields` | `created_at` | `tweets.created_at` |
| `expansions` | `author_id` | `includes.users.id`, `includes.users.name`, `includes.users.username` |
| `user.fields` | `created_at` | `includes.users.created_at` |

  
Once you've added these, the URL in your cURL request should look like the following:

      `https://api.twitter.com/2/tweets/sample/stream?tweet.fields=created_at&expansions=author_id&user.fields=created_at`
    

####   
Step five: Make your request and review your response

Once you have everything set up, you can submit your request to Twitter using a command line tool. If done successfully, you will receive a live stream of Tweets with payloads similar to the following:

      `{   "data": [     {       "author_id": "2244994945",       "created_at": "2020-02-14T19:00:55.000Z",       "id": "1228393702244134912",       "edit_history_tweet_ids": ["1228393702244134912"],       "text": "What did the developer write in their Valentine’s card?\n  \nwhile(true) {\n    I = Love(You);  \n}"     },     {       "author_id": "2244994945",       "created_at": "2020-02-12T17:09:56.000Z",       "id": "1227640996038684673",       "edit_history_tweet_ids": ["1227640996038684673"],       "text": "Doctors: Googling stuff online does not make you a doctor\n\nDevelopers: https://t.co/mrju5ypPkb"     },     {       "author_id": "2244994945",       "created_at": "2019-11-27T20:26:41.000Z",       "id": "1199786642791452673",       "edit_history_tweet_ids": ["1199786642791452673"],       "text": "C#"     }   ],   "includes": {     "users": [       {         "created_at": "2013-12-14T04:35:55.000Z",         "id": "2244994945",         "name": "Twitter Dev",         "username": "TwitterDev"       }     ]   } }`
    

If you would like to close your connection, you can press Control-C in your command line tool on either Mac or Windows systems to break the connection, or you can also close the window. 

#### Using the 10% sampled stream

If you have Enterprise access and are working with the 10% sampled stream, note the following differences:   

* The request URL changes from api.twitter.com/2/tweets/sample/stream to api.twitter.com/2/tweets/sample10/stream.
    
* The 10% sample stream is split into 2 partitions, each requiring a connection request. Use the partition request parameter to indicate which partition you are connecting to:
    
    * /2/tweets/sample10/stream&partition=1
        
    * /2/tweets/sample10/stream&partition=2