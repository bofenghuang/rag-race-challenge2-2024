platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/app/subscriptions


## Creating

You can create new Webhooks subscriptions using this edge:

HTTPPHP SDKAndroid SDKiOS SDK

    POST /v19.0/{app-id}/subscriptions HTTP/1.1
    Host: graph.facebook.com
    
    object=page&callback_url=http%3A%2F%2Fexample.com%2Fcallback%2F&fields=about%2C+picture&include_values=true&verify_token=thisisaverifystring

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{app-id}/subscriptions',
        array (
          'object' => 'page',
          'callback_url' => 'http://example.com/callback/',
          'fields' => 'about, picture',
          'include_values' => 'true',
          'verify_token' => 'thisisaverifystring',
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
    params.putString("object", "page");
    params.putString("callback_url", "http://example.com/callback/");
    params.putString("fields", "about, picture");
    params.putString("include_values", "true");
    params.putString("verify_token", "thisisaverifystring");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/subscriptions",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"object": @"page",
      @"callback_url": @"http://example.com/callback/",
      @"fields": @"about, picture",
      @"include_values": @"true",
      @"verify_token": @"thisisaverifystring",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/subscriptions"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

Making a POST request with the `callback_url`, `verify_token`, and `object` fields will reactivate the subscription.