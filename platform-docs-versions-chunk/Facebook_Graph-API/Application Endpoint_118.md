platform: Facebook
topic: Graph-API
subtopic: Application Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Application Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/app/picture


### Permissions

Because profile pictures are always public on Facebook, this call does not require any access token.

#### Modifiers

| Name | Description | Type |
| --- | --- | --- |
| `redirect` | The `picture` edge is a special case that returns the picture itself by default and not a JSON response. To return a JSON response, you need to set `redirect=false` as a request attribute. This is how you can return the [fields below](#readfields). | `bool` |
| `type` | You can use this to get a pre-specified size of picture. | `enum{small,large}` |

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    GET /v19.0/{app-id}/picture?redirect=0&height=200&type=normal&width=200 HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{app-id}/picture?redirect=0&height=200&type=normal&width=200',
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
        "/{app-id}/picture",
        {
            "redirect": false,
            "height": "200",
            "type": "normal",
            "width": "200"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putBoolean("redirect", false);
    params.putString("height", "200");
    params.putString("type", "normal");
    params.putString("width", "200");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/picture",
        params,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"redirect": @NO,
      @"height": @"200",
      @"type": @"normal",
      @"width": @"200",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/picture"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];