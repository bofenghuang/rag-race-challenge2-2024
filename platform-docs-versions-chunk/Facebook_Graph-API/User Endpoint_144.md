platform: Facebook
topic: Graph-API
subtopic: User Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/User Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/user/scores

### Permissions

As of April 24,2018, the `pubish_actions` permission has been removed. Please see the [Breaking Changes Changelog](https://developers.facebook.com/docs/graph-api/changelog/breaking-changes#login-4-24) for more details. To provide a way for your app users to share content to Facebook, we encourage you to use our [Sharing products](https://developers.facebook.com/docs/sharing) instead.

The **Scores API** is available only for apps that are categorized as Games and have already been granted the `publish_actions` permission in the past.

Please note that `publish_actions` will not be granted for new apps with the sole purpose of accessing this API.

* A user access token with `publish_actions` permission can be used to publish scores for that person.
    
* An app access token can be used if `publish_actions` permission was previously granted.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `score` | The score that you want to set for this person. | `int` |