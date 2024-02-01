platform: Facebook
topic: Graph-API
subtopic: Graph API Overview
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Graph API Overview.md
url: https://developers.facebook.com/docs/graph-api/guides/debugging


## Graph API Debug Mode

When Debug Mode is enabled, Graph API response may contain additional fields that explain potential issues with the request.

To enable debug mode, use the `debug` query string parameter. For example:

cURLAndroid SDKObjective-CJava SDKPHP SDK

    curl -i -X GET \
      "https://graph.facebook.com/{user-id}
        ?fields=friends
        &debug=all
        &access_token={your-access-token}"

    GraphRequest request = GraphRequest.newMeRequest(
      accessToken,
      new GraphRequest.GraphJSONObjectCallback() {
        @Override
        public void onCompleted(JSONObject object, GraphResponse response) {
          // Insert your code here
        }
    });
    
    Bundle parameters = new Bundle();
    parameters.putString("fields", "friends");
    parameters.putString("debug", "all");
    request.setParameters(parameters);
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/{user-id}"
               parameters:@{ @"fields": @"friends",@"debug": @"all",}
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

    FB.api(
      '/{user-id}',
      'GET',
      {"fields":"friends","debug":"all"},
      function(response) {
          // Insert your code here
      }
    );

    try {
      // Returns a `FacebookFacebookResponse` object
      $response = $fb->get(
        '/{user-id}',
        '{access-token}'
      );
    } catch(FacebookExceptionsFacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(FacebookExceptionsFacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();

If `user_friends` permission was not granted, this produces the following response:

{
  "data": \[
  \], 
  "\_\_debug\_\_": {
    "messages": \[
      {
        "message": "Field friends is only accessible on User object, if user\_friends permission is granted by the user", 
        "type": "warning"
      }, 
      {
        "link": "https://developers.facebook.com/docs/apps/changelog#v2\_0", 
        "message": "Only friends who have installed the app are returned in versions greater or equal to v2.0.", 
        "type": "info"
      }
    \]
  }
}

The `debug` parameter value can be set to "all" or to a minimal requested severity level that corresponds to `type` of the message:

| Debug Param Value | What Will Be Returned |
| --- | --- |
| all | All available debug messages. |
| info | Debug messages with type _info_ and _warning_. |
| warning | Only debug messages with type _warning_. |

Debug information, when available, is returned as a JSON object under the `__debug__` key in the `messages` array. Every element of this array is a JSON object that contains the following fields:

| Field | Datatype | Description |
| --- | --- | --- |
| message | String | The message. |
| type | String | The message severity. |
| link | String | \[Optional\] A URL pointing to related information. |

You can also use Debug Mode with [Graph API Explorer](https://developers.facebook.com/tools/explorer).