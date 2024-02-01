platform: Facebook
topic: Graph-API
subtopic: Object Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Object Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/v18.0/object/reactions


### Sample Request

The following example is a `GET` request made by a User who has reacted to their own object.

cURLAndroid SDKObjective-CJava SDKPHP SDK

    curl -i -X GET \
     "https://graph.facebook.com/your-post-id/reactions?access_token=your-user-access-token"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/your-post-id/reactions",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/your-post-id/reactions"
               parameters:nil
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

    FB.api(
      '/your-post-id/reactions',
      'GET',
      {},
      function(response) {
          // Insert your code here
      }
    );

    try {
      // Returns a `FacebookFacebookResponse` object
      $response = $fb->get(
        '/your-post-id/reactions',
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

#### The JSON Response

{
  "data": \[
    {
      "id": "your-user-id",
      "name": "Your Name",
      "type": "HAHA"
    }
  \],
  "paging": {
    "cursors": {
      "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR",
      "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD"
    }
  }
}

If the User or Page has not reacted to the object being queried, `data` will be empty.

The following example is a `GET` request for the total reactions to an object.

cURLAndroid SDKObjective-CJava SDKPHP SDK

    curl -i -X GET \
     "https://graph.facebook.com/your-post-id
       ?fields=reactions.summary(total_count)
       &access_token=your-access-token"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/your-post-id",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    Bundle parameters = new Bundle();
    parameters.putString("fields", "reactions.summary(total_count)");
    request.setParameters(parameters);
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/your-post-id"
               parameters:@{ @"fields": @"reactions.summary(total_count)",}
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

    FB.api(
      '/your-post-id',
      'GET',
      {"fields":"reactions.summary(total_count)"},
      function(response) {
          // Insert your code here
      }
    );

    try {
      // Returns a `FacebookFacebookResponse` object
      $response = $fb->get(
        '/your-post-id',
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

The JSON Response if the User or Page has reacted to their own object.

{
  "reactions": {
    "data": \[
      {
        "id": "your-user-id",
        "name": "Your Name",
        "type": "HAHA"
      }
    \],
    "paging": {
      "cursors": {
        "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR",
        "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD"
      }
    },
    "summary": {
      "total\_count": 28
    }
  },
  "id": "your-post-id"
}

The JSON Response if the User or Page has **not** reacted to their own object.

{
  "reactions": {
    "data": \[
    \],
    "paging": {
      "cursors": {
        "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR",
        "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD"
      }
    },
    "summary": {
      "total\_count": 28
    }
  },
  "id": "your-post-id"
}

A User or Page can only query their own reactions. Other Users' or Pages' reactions are unavailable due to privacy concerns.

The "like" reaction counts include both "like" and "care" reactions.