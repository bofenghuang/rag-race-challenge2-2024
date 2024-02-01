platform: Apple
topic: API-Ad-Repository
subtopic: Ad Repository API
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Apple_API-Ad-Repository/Ad Repository API.md
url: <EMPTY>

Request example

Use ql= URL encoded RSQL filter to allow special characters.



GET ~/api/v1/restrictions

?ql=

actionTaken==ACTION_ADVERTISING_REMOVED;

datePreset==LAST_90_DAYS

\&offset=0

\&limit=50



Request parameters



Parameter Type Required Description



actionTaken string yes

The action taken on the restriction, Values are:

ACTION_ACCOUNT_SUSPENDED

ACTION_ADVERTISING_REMOVED



datePreset string no

The date range of the request. Values are

LAST_90_DAYS, LAST_180_DAYS, LAST_YEAR . The

default is LAST_90_DAYS.



limit integer no The maximum number of entries to return per page.

The default is 50.



offset integer no The offset pagination that limits the number of

returned records. The default is 0.



Ad Repository API January 2024 20

Response example

The restriction object is returned.