platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/comments


### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    POST /v19.0/{object-id}/comments HTTP/1.1
    Host: graph.facebook.com
    
    message=This+is+a+test+comment

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{object-id}/comments',
        array (
          'message' => 'This is a test comment',
        ),
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
        "POST",
        {
            "message": "This is a test comment"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putString("message", "This is a test comment");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{object-id}/comments",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"message": @"This is a test comment",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{object-id}/comments"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];