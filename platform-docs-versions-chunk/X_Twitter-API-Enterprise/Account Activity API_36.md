platform: X
topic: Twitter-API-Enterprise
subtopic: Account Activity API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/X_Twitter-API-Enterprise/Account Activity API.md
url: https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects

Account Activity data objects

## Account Activity data object structure

| Object | Details |
| --- | --- |
| for\_user\_id | Identifies the user subscription subscribed that the event is related to. |
| is\_blocked\_by | (conditional) Shown only when another user mentions your subscribed user. Included if true for Tweet mention events only. |
| source | The user that is performing the activity. For example, the user that is following, blocking, or muting is the source user. |
| target | The user that the activity applies to. For example, the user that is being followed, blocked, or muted is the target user. |