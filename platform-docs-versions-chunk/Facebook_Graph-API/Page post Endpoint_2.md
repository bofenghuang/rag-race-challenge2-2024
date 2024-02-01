platform: Facebook
topic: Graph-API
subtopic: Page post Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Page post Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/page-post/


### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bpage-id%7D_%7Bpost-id%7D%2F&version=v19.0)

    GET /v19.0/{page-id}_{post-id}/ HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{page-id}_{post-id}/',
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
        "/{page-id}_{post-id}/",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{page-id}_{post-id}/",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{page-id}_{post-id}/"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

    curl -X GET -G \
      -d 'access_token=<ACCESS_TOKEN>' \
      https://graph.facebook.com/v19.0/{page-id}_{post-id}/

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).