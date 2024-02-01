platform: Facebook
topic: Instagram-API
subtopic: Instagram API Documentation
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Instagram-API/Instagram API Documentation.md
url: https://developers.facebook.com/docs/instagram-api/overview


## Authorization

Endpoint authorization is handled through [permissions](https://developers.facebook.com/docs/permissions/reference) and [features](https://developers.facebook.com/docs/apps/features-reference). Before your app can use an endpoint to access an app user's Instagram data, you must first request all permissions required by those endpoints from the app user. The app user must then grant those permissions to your app. Once granted, you can query the endpoints to access the user's data.

Note that a permission only allows access to data created by the user who granted the permission. There are a few endpoints that allow apps to access data not created by the app user, but the accessible data is limited and public.

You can request permissions from app users by implementing [Facebook Login](https://developers.facebook.com/docs/facebook-login). App users who have a [role](https://developers.facebook.com/docs/development/build-and-test/app-roles) on your app can grant any requested permissions. App users who do not have a role on your app can only grant permissions and features that have been approved through the [App Review](#app-review) process.

The API uses the following permissions and features:

* [`instagram_basic`](https://developers.facebook.com/docs/permissions/reference/instagram_basic)
* [`instagram_content_publish`](https://developers.facebook.com/docs/permissions/reference/instagram_content_publish)
* [`instagram_manage_comments`](https://developers.facebook.com/docs/permissions/reference/instagram_manage_comments)
* [`instagram_manage_insights`](https://developers.facebook.com/docs/permissions/reference/instagram_manage_insights)
* [`instagram_shopping_tag_products`](https://developers.facebook.com/docs/permissions/reference/instagram_shopping_tag_products)
* [`pages_show_list`](https://developers.facebook.com/docs/permissions/reference/pages_show_list)
* [`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement)
* [Instagram Public Content Access](https://developers.facebook.com/docs/features-reference/instagram-public-content-access)

Refer to our [endpoint reference](https://developers.facebook.com/docs/instagram-api/reference) to determine which permission and features your app will need to request from app users.