platform: X
topic: Twitter-API-V2
subtopic: Fundamentals
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-V2/Fundamentals.md
url: https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/space


## Space

Spaces allow expression and interaction via live audio conversations. The Space data dictionary contains relevant metadata about a Space; all the details are updated in real time.

User objects can found and expanded in the user resource. These objects are available for expansion by adding at least one of host\_ids, creator\_id, speaker\_ids, mentioned\_user\_ids to the expansions query parameter.

Unlike Tweets, Spaces are ephemeral and become unavailable after they end or when they are canceled by their creator. When your app handles Spaces data, you are responsible for returning the most up-to-date information, and must remove data that is no longer available from the platform. The [Spaces lookup endpoints](https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/introduction) can help you ensure you respect the users’ expectations and intent.

| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| id (default) | string | The unique identifier of the requested Space.<br><br>`"id": "1zqKVXPQhvZJB"` | Uniquely identify a Space returned in the response. |
| state (default) | string | Indicates if the Space has started or will start in the future, or if it has ended.<br><br>`"state": "live"` | Filter live or scheduled Spaces. |
| created\_at | date (ISO 8601) | Creation time of this Space.<br><br>`"created_at": "2021-07-04T23:12:08.000Z"` | Understand when a Space was first created and sort Spaces by creation time. |
| ended\_at | date (ISO 8601) | Time when the Space was ended. Only available for ended Spaces. <br><br>`"ended_at": "2021-07-04T00:11:44.000Z"` | Understand when a live Space ended in order to comput its runtime duration. |
| host\_ids | array | The unique identifier of the users who are hosting this Space.<br><br>`"host_ids": [`  <br>  `"2244994945",      "6253282"   ]` | Expand User objects, understand engagement. |
| lang | string | Language of the Space, if detected by Twitter. Returned as a BCP47 language tag.<br><br>`"lang": "en"` | Classify Spaces by inferred language. |
| is\_ticketed | boolean | Indicates is this is a ticketed Space.<br><br>`"is_ticketed": false` | Create user experiences to highlight content of interest. |
| invited\_user\_ids | array | The list of user IDs that were invited to join as speakers. Usually, users in this list are invited to speak via the Invite user option.<br><br>`"mentioned_user_ids": [     "2244994945",      "6253282"   ]` | Expand User objects, understand engagement. |
| participant\_count | integer | The current number of users in the Space, including Hosts and Speakers.<br><br>`"participant_count": 420` | Understand engagement, and create reports and visualizations for creators. |
| subscriber\_count | integer | The number of people who set a reminder to a Space.  <br>`"subscriber_count": 36` | Understand how many people are interested in attending the event. This metric is available for scheduled Spaces and Spaces scheduled in the past that are currently live. |
| scheduled\_start | date (ISO 8601) | Indicates the start time of a scheduled Space, as set by the creator of the Space. This field is returned only if the Space has been scheduled; in other words, if the field is returned, it means the Space is a scheduled Space.<br><br>`"scheduled_start": "2021-07-14T08:00:00.000Z"` | Integrate with calendar notifications, filter and sort Spaces by time. |
| speaker\_ids | array | The list of users who were speaking at any point during the Space. This list contains all the users in **invited\_user\_ids** in addition to any user who requested to speak and was allowed via the Add speaker option.<br><br>`"speaker_ids": [     "2244994945",      "6253282"   ]` | Expand User objects, understand engagement. |
| started\_at | date (ISO 8601) | Indicates the actual start time of a Space.<br><br>`"started_at": "2021-07-14T08:00:12.000Z"` | Determine start time of a Space. |
| title | string | The title of the Space as specified by the creator.<br><br>`"title": "Say hello to the Space data object!"` | Determine the title of a Space, understand referenced keywords, hashtags, and mentions. |
| topic\_ids | array | A list of IDs of the topics selected by the creator of the Space.<br><br>`"topic_ids": [     "2244994945",      "6253282"   ]` | Determine the title of a Space, understand referenced keywords, hashtags, and mentions. |
| updated\_at | date (ISO 8601) | Specifies the date and time of the last update to any of the Space's metadata, such as its title or scheduled time.  <br>`   "updated_at": "2021-07-11T14:44:44.000Z"` | Keep information up to date. |