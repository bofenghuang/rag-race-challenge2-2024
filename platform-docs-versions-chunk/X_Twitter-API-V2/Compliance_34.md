platform: X
topic: Twitter-API-V2
subtopic: Compliance
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Compliance.md
url: https://developer.twitter.com/en/docs/twitter-api/compliance/streams/quick-start


## Steps to build a compliance stream request

#### Step one: Start with a cURL command

In this quick start, we are going to use a simple cURL request to connect to a single partition of the Tweet compliance stream. There are 4 partitions in all, so 4 connections must be maintained to receive all events. The Tweet compliance stream endpoint is a very simple one. All you will have to do is replace or add a couple of elements of the below request and submit it to your command line tool.

      `curl -X GET "https://api.twitter.com/2/tweets/compliance/stream?partition=1" \  -H "Authorization: Bearer $APP_ACCESS_TOKEN"`
    

To connect to the User compliance stream, update the request URL to  "https://api.twitter.com/2/users/compliance/stream?partition=1"

#### Step two: Authenticate your request

Since the compliance stream endpoints require [OAuth 2.0 App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only) authentication, you will need to replace $APP\_ACCESS\_TOKEN with the App Access Token that you generated in the prerequisites. 

#### Step three: Make your request and review your response

Once you have everything set up, you can submit your request to Twitter using the cURL command-line tool. If done successfully, you will receive a live stream of Tweet compliance events with payloads similar to the following:

      `{"data":{"delete":{"tweet":{"id":"1543734217692828673","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.052Z"}}} {"data":{"delete":{"tweet":{"id":"1518339433317514240","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.098Z"}}} {"data":{"delete":{"tweet":{"id":"1543019691868381185","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.156Z"}}} {"data":{"delete":{"tweet":{"id":"1545202024509778944","author_id":"906948460078698496"},"event_at":"2022-07-08T17:54:25.090Z"}}}`
    

If you would like to close your connection, you can press Control-C in your command line tool on either Mac or Windows systems to break the connection, or you can also close the window. 

Your code can parse each JSON line to locate the Tweet (or User ID if using the User compliance stream) and delete the Tweets (or Users) with those IDs from your dataset to stay in compliance.