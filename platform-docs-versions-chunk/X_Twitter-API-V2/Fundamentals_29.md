platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/dm-events


### Sample Request

For this example, we will build a request that retrieves events associated with a one-to-one conversation. This request will return fundamental Direct Message event fields, along with additional fields for referenced Tweets and their authors. Let's build a query that asks for:

* Fundamental event attributes such as when it was created and what conversation it is part of (dm\_conversation).
* The account ID and description of who sent the Direct Message.
* The text of any referenced Tweet, and when it was posted.
* The account ID and description of any referenced Tweet author.

To return those attributes, your request query would include the following:

      `?dm_event.fields=id,sender_id,text,created_at,dm_conversation_id&expansions=sender_id,referenced_tweets.id&tweet.fields=created_at,text,author_id&user.fields=description`
    

      `curl --request GET 'https://api.twitter.com/2/dm_conversations/with/:participant_id/dm_events?tweet.fields=created_at,text,author_id&user.fields=description&expansions=sender_id,participant_ids,referenced_tweets.id&dm_event.fields=id,sender_id,text,participant_ids,created_at,'      --header 'Authorization: Bearer $BEARER_TOKEN'`
    

Be sure to replace $BEARER\_TOKEN with your own generated [Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens).