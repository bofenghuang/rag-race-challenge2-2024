platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting


### Messenger Platform

Rate limits for the Messenger Platform are dependent on the API used and, in some instances, the message content.

#### Messenger API

Requests made by your app are counted against the number of calls your app can make in a rolling 24 hour period and is calculated as follows:

`Calls within 24 hours = 200 * Number of Engaged Users`

The Number of Engaged Users is the number of people the business can message via Messenger.

#### Messenger API for Instagram

Requests made by your app are counted against the number of calls your app can make per Instagram Professional account and the API used.

**Conversations API**

* Your app can make 2 calls per second per Instagram Professional account

**Send API**

* Your app can make 100 calls per second per Instagram Professional account for messages that contain text, links, reactions, and stickers
* Your app can make 10 calls per second per Instagram Professional account for messages that contain audio or video content

**Private Replies API**

* Your app can make 100 calls per second per Instagram Professional account for private replies to Instagram Live comments
* Your app can make 750 calls per hour per Instagram Professional account for private replies to comments on Instagram posts and reels