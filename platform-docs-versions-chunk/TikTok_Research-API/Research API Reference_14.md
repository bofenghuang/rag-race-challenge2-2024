platform: TikTok
topic: Research-API
subtopic: Research API Reference
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Research-API/Research API Reference.md
url: https://developers.tiktok.com/doc/research-api-specs-query-video-comments/


### Body

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Description** |
| data | ResearchVideoCommentsData | A list of comment objects for a given video |
| error | ErrorStructV2 | Error object |

##### ResearchVideoCommentsData

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| comments | CommentObject | The metadata of a comment. | See example below |
| cursor | int64 | The cursor of the next page. | 1050 |
| has\_more | bool | Whether there are more videos or not. | true |

##### Comment Object

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Description** |
| id  | int | The unique ID for the comment |
| text | string | The text within the comment |
| video\_id | int | The ID of the video or item that the comment is under |
| parent\_comment\_id | int | The ID of the comment's parent comment, if any |
| like\_count | int | The number of likes a comment has |
| reply\_count | int | The number of replies a comment has |
| create\_time | int | The unix timestamp that the comment was created on |