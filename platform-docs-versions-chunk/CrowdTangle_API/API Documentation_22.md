platform: CrowdTangle
topic: API
subtopic: API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/CrowdTangle_API/API Documentation.md
url: https://github.com/CrowdTangle/API/wiki/List

# List

### [](#list)List

A List Object represents a list, saved search or saved post list in a dashboard [/lists](https://github.com/CrowdTangle/API/wiki/Lists).

#### [](#properties)Properties

| Property | Type | Descriptions |
| --- | --- | --- |
| title | string | The title of the list as it appears in the dashboard |
| id  | int | The unique identifier of the list in the CrowdTangle system. Use this id when querying by the `listIds` parameters. |
| type | enum (SAVED\_SEARCH, SAVED\_POSTS, LIST) | The type of the list corresponding with its function in the dashboard. |