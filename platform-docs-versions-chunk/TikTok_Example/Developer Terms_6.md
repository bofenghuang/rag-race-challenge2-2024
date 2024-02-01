platform: TikTok
topic: Example
subtopic: Developer Terms
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/TikTok_Example/Developer Terms.md
url: https://developers.tiktok.com/doc/research-api-specs-query-videos/


### QueryVideoResponseData

|     |     |     |
| --- | --- | --- |
| **Field** | **Type** | **Description** |
| videos | list<Video Object> | A list of video objects that match the query |
| cursor | int64 | Returns video results from the given index. |
| has\_more | bool | Whether there are more videos or not. |
| search\_id | string | A search\_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. |

##### Video Object

|     |     |     |
| --- | --- | --- |
| **Field** | **Type** | **Description** |
| "id" | int64 | Unique identifier for the TikTok video. Also called "item\_id" or "video\_id" |
| "create\_time" | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted. (Inherited field from TNS research API) |
| "username" | string | The video's author's username |
| "region\_code" | string | A two digit code for the country the video was posted in |
| "video\_description" | string | The description of the video, also known as the title |
| "music\_id" | int64 | The music\_id used in the video |
| "like\_count" | int64 | The number of likes the video has received. |
| "comment\_count" | int64 | The number of comments the video has received. |
| "share\_count" | int64 | The number of shares the video has received. |
| "view\_count" | int64 | The number of video views the video has received. |
| "effect\_ids" | list<string> | The list of effect ids applied on the video |
| "hashtag\_names" | list<string> | The list of hashtag names that the video participates in |
| "playlist\_id" | int64 | The ID of playlist that the video belongs to |
| "voice\_to\_text" | string | Voice to text and subtitles (for videos that have voice to text features on, show the texts already generated) |