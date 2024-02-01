platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/versioning


### iOS

Each version of the Facebook SDK for iOS that's released is tied to the version that's available on the date of release. This means that if you're upgrading to a new SDK you're also upgrading to the latest API version as well (although you can manually specify any earlier, available API version with [`[FBSDKGraphRequest initWithGraphPath]`](https://developers.facebook.com/docs/reference/ios/current/class/FBSDKGraphRequest/#initWithGraphPath:parameters:)). The API version is listed with the release of each version of the [Facebook SDK for iOS](https://developers.facebook.com/docs/ios).

Much like the JavaScript SDK, the version is prepended to any calls you make to the graph API through the Facebook SDK for iOS. For example, if `v2.7` was the most recent version of the API, the call `/me/friends` - used in the following code sample - will actually call `/v2.7/me/friends`:

\[\[\[FBSDKGraphRequest alloc\] initWithGraphPath:@"me/friends"
  parameters:@{@"fields": @"cover,name,start\_time"}\]
    startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection, id result, NSError \*error) {
        (...)
    }\];

You can override the version of the call with [`[FBSDKGraphRequestConnection overrideVersionPartWith]`](https://developers.facebook.com/docs/reference/ios/current/class/FBSDKGraphRequestConnection/#overrideVersionPartWith:).