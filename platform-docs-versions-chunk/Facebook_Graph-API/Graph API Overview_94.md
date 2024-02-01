platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/error-handling


### Authentication Error Subcodes

| Code | Name | What To Do |
| --- | --- | --- |
| 458 | App Not Installed | The User has not logged into your app. Reauthenticate the User. |
| 459 | User Checkpointed | The User needs to log in at https://www.facebook.com or https://m.facebook.com to correct an issue. |
| 460 | Password Changed | On iOS 6 and above, if the person logged in using the OS-integrated flow, direct them to Facebook OS settings on the device to update their password. Otherwise, they must log in to the app again. |
| 463 | Expired | Login status or access token has expired, been revoked, or is otherwise invalid. [Handle expired access tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#errors). |
| 464 | Unconfirmed User | The User needs to log in at https://www.facebook.com or https://m.facebook.com to correct an issue. |
| 467 | Invalid Access Token | Access token has expired, been revoked, or is otherwise invalid. [Handle expired access tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#errors). |
| 492 | Invalid Session | User associated with the Page access token does not have an appropriate role on the Page. |