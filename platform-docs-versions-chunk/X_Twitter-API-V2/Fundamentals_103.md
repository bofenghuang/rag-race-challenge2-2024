platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/edit-tweets

## 

The examples below demonstrate how a developer can request edited Tweet metadata using the Twitter API v2. 

**Note:** The examples below use the User Tweet Timeline endpoint, but you can request this metadata using the same parameters (with fields and expansions) for all endpoints that return Tweets (e.g. Tweets lookup, search, filtered stream,  etc.)

### Default behavior

By default, an API request to any endpoint that returns Tweet objects in the Twitter API v2, you get:

* The Tweet ID
* The Tweet Text
* An array of Tweet IDs that are part of a Tweet’s edit history. If there is only one ID provided, that means the Tweet has not been edited.

**Request:**

      `curl --request GET 'https://api.twitter.com/2/users/:id/tweets' --header 'Authorization: Bearer $BEARER_TOKEN'`
    

**Sample Response:**

      `{   "data": [     {       "id": "1514991667853602823",       "text": "we have an edit button",       "edit_history_tweet_ids": ["1514991667853602822", "1514991667853602823"]     }   ] }`