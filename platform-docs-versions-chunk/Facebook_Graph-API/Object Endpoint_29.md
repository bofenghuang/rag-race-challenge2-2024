platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/reactions


### Fields

Reading from this edge will return a JSON formatted result

{
    "data": \[\],
    "paging": {},
    "summary": {}
}

`data`

The [Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) of the Page or User running the query, if the object being queried was reacted to by the Page or User, and a list of reaction types:

| Field | Description |
| --- | --- |
| `type`<br><br>enum {NONE, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY} | The type of reaction a Page or User marked an object. |

For reactions on Posts, this edge does not return a Profile except for the current user, if read with a user access token.

#### View the count of an individual reaction

cURLAndroid SDKObjective-CJava SDKPHP SDK

    curl -i -X GET \
     "https://graph.facebook.com/your-object-id
       ?fields=reactions.type(LOVE).limit(0).summary(total_count)
       &access_token=your-access-token"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/your-object-id",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    Bundle parameters = new Bundle();
    parameters.putString("fields", "reactions.type(LOVE).limit(0).summary(total_count)");
    request.setParameters(parameters);
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/your-object-id"
               parameters:@{ @"fields": @"reactions.type(LOVE).limit(0).summary(total_count)",}
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

    FB.api(
      '/your-object-id',
      'GET',
      {"fields":"reactions.type(LOVE).limit(0).summary(total_count)"},
      function(response) {
          // Insert your code here
      }
    );

    try {
      // Returns a `FacebookFacebookResponse` object
      $response = $fb->get(
        '/your-object-id',
        '{access-token}'
      );
    } catch(FacebookExceptionsFacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(FacebookExceptionsFacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();

#### Example JSON Returned

{
  "reactions": {
    "data": \[
    \],
    "summary": {
      "total\_count": 3498
    }
  },
  "id": "your-object-id"
}

`paging`

For more details about pagination, see the Graph API's [paging documentation](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging). Adding `limit(0)` to `reactions` will remove `paging` from the output.

`summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>unsigned int32 | Total number of reactions |
| `viewer_reaction`<br><br>enum {NONE, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY} | The type of reaction a Page or User marked an object. |