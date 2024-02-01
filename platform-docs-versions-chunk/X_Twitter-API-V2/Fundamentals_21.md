platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/poll


## Poll

A poll included in a Tweet is not a primary object on any endpoint, but can be found and expanded in the Tweet object. 

The object is available for expansion with `?expansions=attachments.poll_ids` to get the condensed object with only default fields. Use the expansion with the field parameter: `poll.fields` when requesting additional fields to complete the object.

| Field value | Type | Description |
| --- | --- | --- |
| id (default) | string | Unique identifier of the expanded poll.<br><br>`"id": "1199786642791452673"` |
| options (default) | array | Contains objects describing each choice in the referenced poll.<br><br>`"options": [                      {                          "position": 1,                          "label": "“C Sharp”",                          "votes": 795                      },                      {                          "position": 2,                          "label": "“C Hashtag”",                          "votes": 156                      }                  ]` |
| duration\_minutes | integer | Specifies the total duration of this poll.<br><br>`"duration_minutes": 1440` |
| end\_datetime | date (ISO 8601) | Specifies the end date and time for this poll.<br><br>`"end_datetime": "2019-11-28T20:26:41.000Z"` |
| voting\_status | string | Indicates if this poll is still active and can receive votes, or if the voting is now closed.<br><br>`"voting_status": "closed"` |