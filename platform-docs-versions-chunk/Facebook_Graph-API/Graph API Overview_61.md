platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/versioning

### JavaScript

The JavaScript SDK can only use different API versions if you're [using the `sdk.js` path](https://developers.facebook.com/docs/apps/changelog/#v2_0_js_sdk).

If you're using `FB.init()` from the [JavaScript SDK](https://developers.facebook.com/docs/javascript), you need to use the version parameter, like this:

FB.init({
  appId      : '{app-id}',
  version    : '`v19.0`'
});

If you set the version flag in the init, then any calls to [`FB.api()`](https://developers.facebook.com/docs/javascript/reference/FB.api) will automatically have the version prepended to the path that's called. The same is true for any dialogs for Facebook Login that happen to get called. You will get the Facebook Login dialog for that version of the API.

If you need to, you can override a version by just prepending the version to the path of the endpoint in the `FB.api()` call.