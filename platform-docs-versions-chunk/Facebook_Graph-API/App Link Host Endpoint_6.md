platform: Facebook
topic: Graph-API
subtopic: App Link Host Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/App Link Host Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/app-link-host


## Updating

Facebook apps can update app links using this edge:

PHP SDKHTTPAndroid SDKiOS SDK

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{app-link-host-id}',
        array (
          'name' => 'Updated Name',
          'android' => '[]',
          'web' => '{"should_fallback": true}',
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

    POST /v19.0/{app-link-host-id} HTTP/1.1
    Host: graph.facebook.com
    
    name=Updated+Name&android=%5B%5D&web=%7B%22should_fallback%22%3A+true%7D

    Bundle params = new Bundle();
    params.putString("name", "Updated Name");
    params.putString("android", "[]");
    params.putString("web", "{\"should_fallback\": true}");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-link-host-id}",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"name": @"Updated Name",
      @"android": @"[]",
      @"web": @"{\"should_fallback\": true}",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-link-host-id}"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];