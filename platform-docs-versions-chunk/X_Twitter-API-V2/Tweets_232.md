platform: X
topic: Twitter-API-V2
subtopic: Tweets
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Tweets.md
url: https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/handling-disconnections


### Why a streaming connection might be disconnected

Your stream can disconnect for a number of reasons. Inspect the error message returned by the stream to understand the reason for the failure. Possible reasons for disconnections are as follows:

* An authentication error (such as a wrong token or a wrong authentication method being used).
* A streaming server is restarted on the Twitter side. This is usually related to a code deploy and should be generally expected and designed around.
* Your client is not keeping up with the volume of Tweets the stream is delivering or is reading data too slowly. Every streaming connection is backed by a queue of messages to be sent to the client. If this queue grows too large over time, the connection will be closed.
* Your account exceeded your daily/monthly quota of Tweets.
* You have too many active redundant connections.
* A client stops reading data suddenly. If the rate of Tweets being read off of the stream drops suddenly, the connection will be closed.
* Possible networking issues between server and client
* A temporary server side issue, scheduled maintenance and updates. (Check the [status page](https://api.twitterstat.us/))  
     

#### Common disconnection errors include: 

      `{ 	"errors": [{ 		"title": "operational-disconnect", 		"disconnect_type": "UpstreamOperationalDisconnect", 		"detail": "This stream has been disconnected upstream for operational reasons.", 		"type": "https://api.twitter.com/2/problems/operational-disconnect" 	}] }`
    

      ` { 	"title": "ConnectionException", 	"detail": "This stream is currently at the maximum allowed connection limit.", 	"connection_issue": "TooManyConnections", 	"type": "https://api.twitter.com/2/problems/streaming-connection" }`