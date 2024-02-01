platform: Facebook
topic: Content-Library-API
subtopic: Content-Library-API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Content-Library-API/Content-Library-API Documentation.md
url: https://developers.facebook.com/docs/content-library-api/data


## Instagram post

| Name | API field | Description | Products |
| --- | --- | --- | --- |
| Meta Content Library ID | id  | The Meta Content Library ID associated with the Instagram post. | Content Library API |
| Text | text | The text of the Instagram post. Tags are excluded. | Content Library<br><br>  <br><br>Content Library API |
| Creation time | creation\_time | The time the Instagram post was created. | Content Library<br><br>  <br><br>Content Library API |
| Modified time | modified\_time | The time the Instagram post was most recently modified. | Content Library API |
| Language | lang | The content language of the Instagram post. Returns ISO 639-1 language code in 2-letter lowercase format. | Content Library API |
| Comments | statistics.comment\_count | The number of comments on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Likes | statistics.like\_count | The number of like reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Views | statistics.views | The number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. For video posts, views are counted whether the video was played or not. Only posts with more than 100 views display the view count. A post displays no view count value if there were fewer than 100 views as of the last refresh. View counts for Instagram posts or reels made before October 1, 2022 are not available. View counts are not available for Instagram posts created in the last 3-5 days due to the refresh cycle. | Content Library<br><br>  <br><br>Content Library API |
| View counts last refreshed date | view\_date\_last\_refreshed | The date the view count was last refreshed. View counts are refreshed every 3 days for all Instagram posts and reels. | Content Library<br><br>  <br><br>Content Library API |
| Post owner account type | post\_owner.type | The account type of the post owner associated with the Instagram post. Post owner types include business, creator, and personal. For personal accounts, only those with privacy [set to public](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F517073653436611&h=AT0RgShRVvlHXcEl2J9_VJ7rsUDXaqFBtFsc2IsJGhO7TnG1VYjEURs_l-Xwi5co1LDJkTIY4VS_NKpIGeW9OJE56wEH5uD0Fn2aPYNRoTReTsyMYUCYEtbARdY8jktrS8lYlyRREGtqlIEo) and with either a verified badge or 50,000 or more followers are included. A [verified badge](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F733907830039577%3Fhelpref%3Dfaq_content&h=AT3l6a8eoqRxtcQBUbFK85rjLZk0jbJFtuz0q7_icHHXKzgkHiXCiW6yJL_p6Nxf38resgDJJzWJA_pNSzpNyoir4M_rbssr-hyj9p_b8Q13Gcnntskrp5PuNl1ACcMtMIQvzpOAnLfy6TnX) in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription. | Content Library API |
| Post owner ID | post\_owner.id | The Meta Content Library ID of the owner associated with the Instagram post. | Content Library API |
| Is branded content | is\_branded\_content | Whether the Instagram post has branded content or not. [Learn more.](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1123581461537025%2F&h=AT3ZdyvyC8cShDadIO7KI432Xs5hqirOW4UeI9nYmSefhdUB17Cp6XVG9evr6z_pvWyBVbScqSrDjfutOXNDm31CqZkeW0a_7cDTs9tBVFtBDptk8DDWYtraKX_Dy_nJKgMmCyJT63Igkoxv) | Content Library API |
| Media type | media\_type | The media type included in the Instagram post. Media types include albums, photos, and videos and reels. | Content Library<br><br>  <br><br>Content Library API |
| Hashtags | hashtags | The list of hashtags included in the Instagram post. | Content Library<br><br>  <br><br>Content Library API |