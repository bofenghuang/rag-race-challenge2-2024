platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/migrate/standard-to-twitter-api-v2


### Similarities

#### Authentication 

The v1.1 statuses/user\_timeline and the Twitter API v2 user Tweet timeline endpoint support both [OAuth 1.0a User Context](https://developer-staging.twitter.com/en/docs/authentication/oauth-1-0a) and [OAuth 2.0 App-Only](https://developer-staging.twitter.com/en/docs/authentication/oauth-2-0). Therefore, you can continue using the same authentication method and authorization tokens if you migrate to the Twitter API v2 version.   
 

#### Historical Access

The v1.1 statuses/user\_timeline and the Twitter API v2 user Tweet timeline endpoint both will return the most recent 3200 Tweets, including Retweets

The v1.1 statuses/mentions\_timeline and the Twitter API v2 user mention timeline endpoint can return the most recent 800 Tweets.  
 

**Support for Tweet edit history and metadata**  

Both versions provide metadata that describes any edit history. Check out the [filtered stream API References](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference) and the [Edit Tweets fundamentals page](https://developer.twitter.com/en/docs/twitter-api/edit-tweets) for more details. 

#### Rate Limits

|     |     |
| --- | --- |
| **Standard v1.1** | **Twitter API v2** |
| user\_timeline:<br><br>900 requests per 15 min with OAuth 1.0a User Context<br><br>1500 requests per 15 min with OAuth 2.0 App-Only | User Tweets timeline:<br><br>900 requests per 15-minute window with OAuth 1.0a User Context<br><br>1500 requests per 15-minute window with OAuth 2.0 App-Only |

#### Refresh polling using since\_id

Both versions allow polling for recent results using the since\_id.  
 

#### Traversing timelines by Tweet IDs

Both endpoints have the capability to traverse through timelines using Tweet ID 'timestamps' based on the way Twitter IDs are constructed.  The functionality is generally  the same except for the following:

|     |     |
| --- | --- |
| **Standard timelines v1.1** | **timelines v2** |
| since\_id (exclusive)<br><br>max\_id (inclusive) | since\_id (exclusive)<br><br>until\_id (also exclusive, vs max\_id which was inclusive) |

#### Response filtering parameters

|     |     |
| --- | --- |
| **Standard timelines v1.1** | **timelines v2** |
| Response filtering parameters:<br><br>* include\_rts<br>* exclude\_replies | Response filtering parameters:<br><br>* exclude=retweets,replies |
| Example <br><br>https://api.twitter.com/1.1/statuses/user\_timeline.json?user\_id=2244994945&include\_rts=0&&exclude\_replies=1 | Example:<br><br>https://api.twitter.com/2/users/2244994945/tweets?max\_results=100&exclude=retweets,replies |
| Notes:<br><br>For user\_timeline:<br><br>* Using include\_rts=0 does not change the possible historical Tweet limit of the most recent 3200 | Notes:<br><br>For user Tweets timeline:<br><br>* Using exclude=retweets does not change the possible historical Tweet limit of the most recent  3200 <br>* Using exclude=replies reduces the possible historical Tweet limit to the most recent 800 replies |