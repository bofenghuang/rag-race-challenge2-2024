platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/overview


## 

Enterprise

The Account Activity API provides you the ability to subscribe to realtime activities related to a user account via webhooks. This means that you can receive realtime Tweets, Direct Messages, and other account events from one or more of your owned or subscribed accounts through a single connection.

You will receive all related activities below for each user subscription on your webhook registration:

| Activity types |     |
| --- | --- |
| * Tweets (by user)  <br>    <br>* Tweet deletes (by user)<br>* @mentions (of user)<br>* Replies (to or from user)<br>* Retweets (by user or of user)<br>* Quote Tweets (by user or of user)<br>* Retweets of Quoted Tweets (by user or of user)<br>* Likes (by user or of user)<br>* Follows (by user or of user)  <br>    <br>* Unfollows (by user) | * Blocks (by user)<br>* Unblocks (by user)<br>* Mutes (by user)<br>* Unmutes (by user)<br>* Direct Messages sent (by user)<br>* Direct Messages received (by user)<br>* Typing indicators (to user)<br>* Read receipts (to user)<br>* Subscription revokes (by user) |

**Please note** - We do not deliver home timeline data via the Account Activity API. Please use the [GET statuses/home\_timeline](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-home_timeline) to pull this data.  
 

#### Video Series

Check out our [four-part video series](https://www.youtube.com/watch?v=otPxejFhyy8&index=0&list=PLFKjcMIU2WshGG6Yj940XM7Z6BFs1zfBg) on the Account Activity API to get up to speed!

> Today we announced the Account Activity API is generally available as a premium and enterprise API. 🔔 [pic.twitter.com/xnlF9kPevi](https://t.co/xnlF9kPevi)
> 
> — Twitter Dev (@TwitterDev) [May 16, 2018](https://twitter.com/TwitterDev/status/996790447048613888?ref_src=twsrc%5Etfw)