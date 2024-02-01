platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/comments


### Parameters

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    GET /v19.0/{object-id}/comments?summary=1&filter=toplevel HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{object-id}/comments?summary=1&filter=toplevel',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{object-id}/comments",
        {
            "summary": true,
            "filter": "toplevel"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putBoolean("summary", true);
    params.putString("filter", "toplevel");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{object-id}/comments",
        params,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"summary": @YES,
      @"filter": @"toplevel",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{object-id}/comments"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

| Parameter | Description |
| --- | --- |
| `summary`<br><br>_bool_ | A summary of metadata about the comments on the object. Importantly this metadata includes `order` which indicates how the comments are being sorted. |
| `filter`<br><br>_enum { toplevel, stream }_ | If a person can reply to a comment, you can filter comments based on top level comments, comments that are made directly on the post, or the chronological order of all comments.<br><br>* `toplevel` - This is the default. It returns all top-level comments in chronological order, as ordered on Facebook. This filter is useful for displaying comments in the same structure as they appear on Facebook.<br>* `stream` - All-level comments in `chronological` order. This filter is useful for comment moderation tools where it is helpful to see a chronological list of all comments. |