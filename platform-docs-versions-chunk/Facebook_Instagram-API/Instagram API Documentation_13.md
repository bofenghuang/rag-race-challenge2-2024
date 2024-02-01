platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/overview


## Tasks

In order for an app user to grant your app permissions, the app user must be able to perform [tasks](https://developers.facebook.com/docs/pages/access-tokens#page-tasks) on the Facebook Page connected to the Instagram account they are attempting to access. App users may grant your app permissions based on tasks they are able to perform as follows:

| Permission | `MANAGE` | `CREATE_CONTENT` | `MODERATE` | `ADVERTISE` | `ANALYZE` |
| --- | --- | --- | --- | --- | --- |
| instagram\_basic | ✔   | ✔   | ✔   | ✔   | ✔   |
| instagram\_content\_publish | ✔   | ✔   |     |     |     |
| instagram\_manage\_comments | ✔   | ✔   | ✔   |     |     |
| instagram\_manage\_insights | ✔   | ✔   | ✔   | ✔   | ✔   |

You can determine which tasks an app user is able to perform on a Page by querying the [`GET /me/accounts`](https://developers.facebook.com/docs/graph-api/reference/user/accounts#Reading) endpoint with the app user's User access token. The endpoint will return a list of Pages that the app user is able to perform tasks on, and indicate which tasks the user can perform on each of them.

Refer to the [reference documentation](https://developers.facebook.com/docs/instagram-api/reference/) to see which permissions each endpoint requires. The API does not support [Business Manager System Users](https://developers.facebook.com/docs/marketing-api/system-users), or app users who have the Live Contributor role.