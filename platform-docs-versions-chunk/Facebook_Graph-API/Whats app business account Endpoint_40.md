platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/product_catalogs/


### Example

Requirements

* whatsapp\_business\_management permission
    
* whatsapp\_business\_messaging permission
    
* catalog\_management permission
    
* public\_profile permission
    
* WHATSAPP BUSINESS ACCOUNT ID
    
* USER ACCESS TOKEN
    

Request

cURLAndroid SDKObjective-C

    curl -i -X GET \
     "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID/product_catalogs?access_token=USERS-ACCESS-TOKEN"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/WHATSAPP-BUSINESS-ACCOUNT-ID/product_catalogs",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID/product_catalogs"
               parameters:nil
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

Response

{
  "data": \[
  \]
}