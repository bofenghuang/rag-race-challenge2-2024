platform: Facebook
topic: Graph-API
subtopic: Group Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Group Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/group/albums


## Publishing

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    POST /v19.0/{group-id}/albums HTTP/1.1
    Host: graph.facebook.com
    
    name=%7Balbum-name%7D&message=%7Balbum-description%7D&privacy=%7Bprivacy-settings%7D

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{group-id}/albums',
        array (
          'name' => '{album-name}',
          'message' => '{album-description}',
          'privacy' => '{privacy-settings}',
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
        "/{group-id}/albums",
        "POST",
        {
            "name": "{album-name}",
            "message": "{album-description}",
            "privacy": "{privacy-settings}"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putString("name", "{album-name}");
    params.putString("message", "{album-description}");
    params.putString("privacy", "{privacy-settings}");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{group-id}/albums",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"name": @"{album-name}",
      @"message": @"{album-description}",
      @"privacy": @"{privacy-settings}",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{group-id}/albums"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];