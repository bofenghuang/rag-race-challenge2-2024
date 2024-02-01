platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/api-reference/get-dm_conversations-with-participant_id-dm_events

### Example code with offical [SDKs](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/sdks/overview)

* [cURL (default fields)](#tab0)
* [cURL (optional fields)](#tab1)

cURL (default fields)

cURL (optional fields)

      `curl "https://api.twitter.com/2/dm_conversations/with/:participant_id/dm_events" -H "Authorization: Bearer $ACCESS_TOKEN"`
    

      `curl "https://api.twitter.com/2/dm_conversations/with/:participant_id/dm_events?dm_event.fields=id,text,event_type,dm_conversation_id,created_at,sender_id,attachments,participant_ids,referenced_tweets" -H "Authorization: Bearer $ACCESS_TOKEN"`