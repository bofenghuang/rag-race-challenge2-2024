platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/data


## Facebook post

| Name | API field | Description | Products |
| --- | --- | --- | --- |
| Meta Content Library ID | id  | The Meta Content Library ID associated with the Facebook post. | Content Library API |
| Text | text | The text of the Facebook post. Tags are excluded. | Content Library<br><br>  <br><br>Content Library API |
| Creation time | creation\_time | The time the Facebook post was created. | Content Library<br><br>  <br><br>Content Library API |
| Modified time | modified\_time | The time the Facebook post was most recently modified. | Content Library API |
| Language | lang | The content language of the Facebook post. Returns ISO 639-1 language code in 2-letter lowercase format. | Content Library (Filter only)<br><br>  <br><br>Content Library API |
| Likes | statistics.like\_count | The number of like reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Love reactions | statistics.love\_count | The number of love reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Wow reactions | statistics.wow\_count | The number of wow reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Haha reactions | statistics.haha\_count | The number of haha reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Sad reactions | statistics.sad\_count | The number of sad reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Angry reactions | statistics.angry\_count | The number of angry reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Comments | statistics.comment\_count | The number of comments on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Reactions | statistics.reaction\_count | The total number of reactions on the post. Reactions include: Like, Love, Care, Haha, Wow, Sad or Angry. | Content Library<br><br>  <br><br>Content Library API |
| Shares | statistics.share\_count | The number of times the post was shared. | Content Library<br><br>  <br><br>Content Library API |
| Care reactions | statistics.care\_count | The number of care reactions on the post. | Content Library<br><br>  <br><br>Content Library API |
| Views | statistics.views | The number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. For video posts, views are counted whether the video was played or not. Only posts with more than 100 views display the view count. A post displays no view count value if there were fewer than 100 views as of the last refresh. View counts for Facebook posts or reels made before January 1, 2017 are not available. View counts are not available for Facebook posts created in the last 5-7 days due to the refresh cycle. | Content Library<br><br>  <br><br>Content Library API |
| View counts last refreshed date | view\_date\_last\_refreshed | The date the view count was last refreshed. View counts are refreshed every 7 days for all Facebook posts. | Content Library<br><br>  <br><br>Content Library API |
| Post owner type | post\_owner.data.type | The type of post owner associated with the Facebook post. Post owner types include: Pages, groups and events. | Content Library<br><br>  <br><br>Content Library API |
| Post owner ID | post\_owner.data.id | The Meta Content Library ID of the owner associated with the Facebook post. | Content Library API |
| Post owner name | post\_owner.data.name | The name of the post owner associated with the Facebook post. | Content Library<br><br>  <br><br>Content Library API |
| Media type | media\_type | The media type included in the Facebook Post. Media types include photos, videos and reels, and miscellaneous (including links, reshares, and text-only posts). | Content Library |
| Branded content Page ID | branded\_content\_page\_id | The Meta Content Library ID of the Page associated with the Facebook post. Included if the post has branded content. [Learn more.](https://www.facebook.com/business/help/788160621327601?id=1912903575666924) | Content Library API |
| Link attachment fields description | link\_attachment\_fields.description | The description of the link attachment included in the Facebook post. | Content Library API |
| Link attachment fields link | link\_attachment\_fields.link | The URL of the link attachment included in the Facebook post. | Content Library API |
| Link attachment fields name | link\_attachment\_fields.name | The name of the link attachment included in the Facebook post. | Content Library API |
| Link attachment fields caption | link\_attachment\_fields.caption | The caption of the link attachment included in the Facebook post. | Content Library API |
| Shared post ID | shared\_post\_id | The Meta Content Library ID of the reshared post included in the Facebook post. | Content Library API |