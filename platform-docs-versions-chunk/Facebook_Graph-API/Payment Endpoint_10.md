platform: Facebook
topic: Graph-API
subtopic: Payment Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Payment Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/payment/refunds


## Publishing

You can use this edge to initiate refunds:

HTTPPHP SDKAndroid SDKiOS SDK

    POST /v19.0/{payment-id}/refunds HTTP/1.1
    Host: graph.facebook.com
    
    currency=EUR&amount=1.00

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{payment-id}/refunds',
        array (
          'currency' => 'EUR',
          'amount' => '1.00',
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
    params.putString("currency", "EUR");
    params.putString("amount", "1.00");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{payment-id}/refunds",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"currency": @"EUR",
      @"amount": @"1.00",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{payment-id}/refunds"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];