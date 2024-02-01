platform: Facebook
topic: Graph-API
subtopic: Comment Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Comment Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/comment


### Permissions

* **General** - To read a comment, you generally need the same permissions as required for viewing the object that the comment was added to.
    
* **Replies** - If this is a comment that is a reply to another comment, the permissions required apply to the object that the parent comment was added to.
    
* **Page owned Comments and Replies** — For any comments or replies owned by (on) a Page, you must use a Page access token if you want User information to be included in the response.
    

The Page Post comment ID format, `{page-id}_{post_id}_{comment-id}`, has been deprecated. Use the `{pagepost-id}_{comment-id}` format instead.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcomment-id%7D&version=v19.0)

    GET /v19.0/{comment-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{comment-id}',
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
        "/{comment-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{comment-id}",
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
                                   initWithGraphPath:@"/{comment-id}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];