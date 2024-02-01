platform: Facebook
topic: Graph-API
subtopic: Event Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Event Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/event/picture


### Permissions

* A user access token is required to retrieve the cover photo of any events visible to that person.
    

#### Modifiers

| Name | Description | Type |
| --- | --- | --- |
| `redirect` | The `picture` edge is a special case, as when requested, it will by default return the picture itself and not a JSON response. To return a JSON response, you need to set `redirect=false` as a request attribute. This is how to return the [fields below](#readfields). | `bool` |
| `type` | You can use this to get a pre-specified size of picture. | `enum{small, normal, large, square}` |

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    GET /v19.0/{event-id}/picture?redirect=0&type=normal HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{event-id}/picture?redirect=0&type=normal',
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
        "/{event-id}/picture",
        {
            "redirect": false,
            "type": "normal"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putBoolean("redirect", false);
    params.putString("type", "normal");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{event-id}/picture",
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
      @"type": @"normal",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{event-id}/picture"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];