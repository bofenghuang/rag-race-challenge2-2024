platform: Facebook
topic: Graph-API
subtopic: Test user Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Test user Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/test-user


## Publishing and Updating

You can publish to this node to update the test user's password or name.

HTTPPHP SDKAndroid SDKiOS SDK

    POST /v19.0/{test-user-id} HTTP/1.1
    Host: graph.facebook.com
    
    password=newpassword&name=Newname+Smith

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{test-user-id}',
        array (
          'password' => 'newpassword',
          'name' => 'Newname Smith',
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

    Bundle params = new Bundle();
    params.putString("password", "newpassword");
    params.putString("name", "Newname Smith");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{test-user-id}",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"password": @"newpassword",
      @"name": @"Newname Smith",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{test-user-id}"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];