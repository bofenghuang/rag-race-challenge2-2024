platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/overview


### Referring to tasks

If you need to inform your app users about tasks (and which ones are required to use your app properly), here's how tasks are referred to in our various UIs.

#### Classic Pages

[Classic Pages](https://www.facebook.com/help/135275340210354) refer to tasks as **roles**. App users with an Admin role on a Page can grant your app any permission. App users with other roles can grant permissions as follows:

| Role | Grantable Permissions |
| --- | --- |
| Editor | instagram\_basic  <br>instagram\_content\_publish |
| Moderator | instagram\_basic  <br>instagram\_manage\_comments  <br>instagram\_manage\_insights |
| Advertiser | instagram\_basic  <br>instagram\_manage\_insights |
| Analyst | instagram\_basic  <br>instagram\_manage\_insights |

#### New Experience Pages

[New Experience Pages](https://www.facebook.com/business/help/782660422528806) refer to tasks as either Facebook Access or Task Access. App users with Facebook Access on a Page can grant your app any permission. App users with Task Access can grant permissions as follows:

| Task Access | Grantable Permissions |
| --- | --- |
| Ads | instagram\_basic |
| Content | instagram\_basic  <br>instagram\_content\_publish |
| Insights | instagram\_basic  <br>instagram\_manage\_insights |
| Messages & Community Activity | instagram\_basic  <br>instagram\_manage\_comments |

To determine if a Page is using the new experience, request its [`has_transitioned_to_new_page_experience`](https://developers.facebook.com/docs/graph-api/reference/page/#Reading) field. This value return `true` if the Page uses the new experience.

[](#)