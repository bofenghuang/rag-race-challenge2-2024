platform: X
topic: Twitter-API-V2
subtopic: Direct Messages
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Direct Messages.md
url: https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/integrate


### Conversation event types

Below are example JSON objects for Direct Message the MessageCreate, ParticipantsJoin, and ParticipantsLeave event types.   

Available dm\_event object fields: id, text, event\_type, dm\_conversation\_id, created\_at, sender\_id, attachments, referenced\_tweets, participant\_ids. See the the Fields and Expansion section for more details on selecting these fields in your requests.   

Example MessageCreate event: 

With all the dm\_event fields specified, here is the response for a simple text Direct Message: 

      `{     "text": "Hi everyone.",     "sender_id": "944480690",     "dm_conversation_id": "1578398451921985538",     "id": "1582838499983564806",     "event_type": "MessageCreate",     "created_at": "2022-10-19T20:58:00.000Z" }`
    

Example ParticipantsJoin event:

With all the dm\_event fields specified, here is the response for a participant joining a conversation:

      `{     "participant_ids": [         "944480690"     ],     "sender_id": "17200003",     "dm_conversation_id": "1578398451921985538",     "id": "1582835469712138240",     "event_type": "ParticipantsJoin",     "created_at": "2022-10-19T20:45:58.000Z" }`
    

Example ParticipantsLeave event:

With all the dm\_event fields specified, here is the response for a participant leaving a conversation:

      `{     "participant_ids": [         "944480690"     ],     "dm_conversation_id": "1578398451921985538",     "id": "1582838535115067392",     "event_type": "ParticipantsLeave",     "created_at": "2022-10-19T20:58:09.000Z"     }`