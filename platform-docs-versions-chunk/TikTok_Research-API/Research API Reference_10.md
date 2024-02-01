platform: TikTok
topic: Research-API
subtopic: Research API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Reference.md
url: https://developers.tiktok.com/doc/research-api-specs-query-user-info/

### Body

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Description** |
| data | User Info Object | The returned user info data |
| error | ErrorStructV2 | Error object |

User Info Object

|     |     |     |
| --- | --- | --- |
| Field name | Type | Description |
| "display\_name" | string | The user's display name / nickname |
| "bio\_description" | string | The user's bio description |
| "avatar\_url" | string | The url to a user's profile picture |
| "is\_verified" | bool | The user's verified status. True if verified, false if not |
| "following\_count" | int | The number of people the user is following |
| "follower\_count" | int | The number of followers the user has |
| "video\_count" | int | The number of videos the user has posted |
| "likes\_count" | int | The total number of likes the user has accumulated |