platform: Facebook
topic: Graph-API
subtopic: Payment Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Payment Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/payment/dispute


## Publishing

You can use this edge to settle disputes:

HTTPPHP SDKAndroid SDKiOS SDK

    POST /v19.0/{payment-id}/dispute HTTP/1.1
    Host: graph.facebook.com
    
    reason=DENIED_REFUND

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{payment-id}/dispute',
        array (
          'reason' => 'DENIED_REFUND',
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
    params.putString("reason", "DENIED_REFUND");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{payment-id}/dispute",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"reason": @"DENIED_REFUND",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{payment-id}/dispute"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];