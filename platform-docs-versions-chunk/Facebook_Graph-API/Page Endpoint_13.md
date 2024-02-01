platform: Facebook
topic: Graph-API
subtopic: Page Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page/


### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=%7Bpage-id%7D%2Fsubscribed_apps%3Fsubscribed_fields%3Dleadgen&version=v19.0)

    POST /v19.0/{page-id}/subscribed_apps HTTP/1.1
    Host: graph.facebook.com
    
    subscribed_fields=leadgen

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{page-id}/subscribed_apps',
        array (
          'subscribed_fields' => 'leadgen',
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
        "/{page-id}/subscribed_apps",
        "POST",
        {
            "subscribed_fields": "leadgen"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putString("subscribed_fields", "leadgen");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{page-id}/subscribed_apps",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"subscribed_fields": @"leadgen",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{page-id}/subscribed_apps"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

    curl -X POST \
      -F 'subscribed_fields="leadgen"' \
      -F 'access_token=<ACCESS_TOKEN>' \
      https://graph.facebook.com/v19.0/{page-id}/subscribed_apps

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).