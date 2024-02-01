platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/guides/webhooks


## Receive Live Webhook Notifications

To receive live webhook notifications, the following conditions must be satisfied:

* Your app must have **Instagram** webhooks configured and appropriate **fields** subscribed to in the App Dashboard.
* For [Consumer apps](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#consumer), they must be in [Live Mode.](https://developers.facebook.com/docs/development/build-and-test/app-modes#live-mode)
* For [Business apps](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#business), they must have permissions with an [Advanced Access](https://developers.facebook.com/docs/graph-api/overview/access-levels#advanced-access) level. You can request Advanced Access for permissions as shown here:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/277167266_482444906912677_1666124645911161205_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=Gc0vUsFmmLEAX8JpXAg&_nc_oc=AQkSGobr2bbUWaCQI4Dmlf6z4ARRm_76lTdKFGKtx5IW8UOgwDcAeDoh6-7SaA9UIm8&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDb8zmWj5CDkj1mU2rKoZzZOHRb0_mqNcWDvFI8CfJx1A&oe=65C000D0)

If the app permissions don't have an access level of **Advanced Access**, the app doesn't receive webhook notifications.

* The app user must have granted your app appropriate permissions ([instagram\_manage\_insights](https://developers.facebook.com/docs/permissions/reference/instagram_manage_insights) for Stories, [instagram\_manage\_comments](https://developers.facebook.com/docs/permissions/reference/instagram_manage_comments) for Comments and @Mentions).
* The Page connected to the app user's account must have [Page subscriptions enabled](https://developers.facebook.com/docs/instagram-api/guides/webhooks/#step-2--enable-page-subscriptions).
* The Business connected to the app user's Page must be **verified**.
* The owner of the Media object upon which the comment or @mention appears must not have set their account to [private](https://www.facebook.com/help/instagram/448523408565555).