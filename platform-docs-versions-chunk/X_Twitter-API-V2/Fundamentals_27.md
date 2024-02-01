platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/dm-events


# Direct Message events

Direct Message (DM) conversations are made up of events. The Twitter API v2 currently supports three event types: MessageCreate, ParticipantsJoin, and ParticipantsLeave.

DM event objects are returned by the [Direct Message lookup](https://developer.twitter.com/en/docs/twitter-api/direct-messages/lookup/introduction) endpoints, and a MessageCreate event is created when Direct Messages are successfully created with the [Manage Direct Messages](https://developer.twitter.com/en/docs/twitter-api/direct-messages/manage/introduction) endpoints.

When requesting DM events, there are three default event object attributes, or fields, included: id, event\_type, and text. To receive additional event fields, use the [fields](https://developer.twitter.com/en/docs/twitter-api/fields) parameter dm\_event.fields to select others. Other available event fields include the following: dm\_conversation\_id, created\_at, sender\_id, attachments, participant\_ids, and referenced\_tweets.

Several of these fields provide the IDs of other Twitter objects related to the Direct Message event:

* sender\_id - The ID of the account that sent the message, or who invited a participant to a group conversation
* partricipants\_ids - An array of account IDs. For ParticipantsJoin and ParticipantsLeave events this array will contain a single ID of the account that created the event
* attachments - Provides media IDs for content that has been uploaded to Twitter by the sender
* referenced\_tweets - If a Tweet URL is found in the text field, the ID of that Tweet is included in the response

The sender\_id, participant\_ids, referenced\_tweets.id, and attachments.media\_keys [expansions](https://developer.twitter.com/en/docs/twitter-api/expansions) are available to expand on these Twitter object IDs.

|     |     |     |     |
| --- | --- | --- | --- |
| **Field value** | **Type** | **Description** | **How it can be used** |
| id (default) | string | The unique identifier of the event.<br><br>"id": "1050118621198921728" | Use this to programmatically retrieve a specific conversation event (available with v1.1 endpoints). |
| event\_type (default) | string | Describes the type of event. Three types are currently supported: <br><br>* MessageCreate<br>    <br>* ParticipantsJoin<br>    <br>* ParticipantsLeave<br>    <br><br>"event\_type": "MessageCreate" | When retrieving a conversation's history, understanding when messages were created, and for group conversations, understanding when participants joined and left. All GET methods support filtering on specific event types with the event\_type= query parameter. . |
| text (default) | string | The actual UTF-8 text of the Direct Message. <br><br>"text": "Hello, just you!" | With chatbots, this can be used to analyze message contents and determining automated responses. Could be used to build conversation search features. |
| sender\_id | string | ID of the User creating the event. To expand this object in the response, include sender\_id as an expansion  and use the user.fields query parameter to specify User object attributes of interest.<br><br>"sender\_id": "906948460078698496" | Retrieve the User object of who created the MessageCreate or ParticipantsJoin event. |
| participant\_id | array (of strings) | IDs of the participants joining and leaving a group conversation. Also used when creating new group conversations. To expand this object in the response, include participant\_ids as an expansion and use the user.fields query parameter to specify User object attributes of interest.<br><br>"participant\_ids": \[<br><br>     "906948460078698496"<br><br>\] | Used to retrieve User objects for participants joining and leaving group conversations. |
| dm\_conversation\_id | string | The unique identifier of the conversation the event is apart of.<br><br>"dm\_conversation\_id": "1584988213961031680" | Use this to programmatically retrieve events from a conversation, and add Direct Messages to it. |
| created\_at | date (ISO 8601) | Creation time (UTC) of the Tweet.<br><br>"created\_at": "2019-06-04T23:12:08.000Z" | This field can be used to understand when a Direct Message was created or when conversation participants joined or left. |
| referenced\_tweets | array | ID for any Tweet mentioned in the Direct Message text. To expand this object in the response, include referenced\_tweets.id as an expansion and use the tweet.fields query parameter to specify Tweet object attributes of interest.<br><br>"referenced\_tweets": \[<br><br>    {<br><br>        "id": "1578868150510456833"<br><br>    }<br><br>\] | When Direct Messages reference a Tweet, these IDs can be used to lookup the Tweet's details. |
| attachments | object | For Direct Messages with attached Media, provides the media key of the uploaded content (photo, video, or GIF. To expand this object in the response, include attachments.media\_keys as an expansion and use the media.fields query parameter to specify media object attributes of interest. Currently, one attachment is supported. <br><br>"attachments": {<br><br>    "media\_keys": \[<br><br>        "3\_1136048009270239232"<br><br>    \]<br><br>} | Understanding the media objects attached to Direct Messages. |