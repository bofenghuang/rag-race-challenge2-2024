platform: Facebook
topic: Graph-API
subtopic: Whats app business account Endpoint
file_path: /home/bhuang/nlp/rag-race-challenge2-2024/platform-docs-versions/Facebook_Graph-API/Whats app business account Endpoint.md
url: https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account/


### Example

Requirements

* whatsapp\_business\_management permission
    
* whatsapp\_business\_messaging permission
    
* public\_profile permission
    
* WhatsApp Business Account (WABA) ID
    
* USER ACCESS TOKEN
    

Request

cURLAndroid SDKObjective-C

    curl -i -X GET \
     "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID?access_token=USER-ACCESS-TOKEN"

    GraphRequest request = GraphRequest.newGraphPathRequest(
      accessToken,
      "/WHATSAPP-BUSINESS-ACCOUNT-ID",
      new GraphRequest.Callback() {
        @Override
        public void onCompleted(GraphResponse response) {
          // Insert your code here
        }
    });
    
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/WHATSAPP-BUSINESS-ACCOUNT-ID"
               parameters:nil
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

Response

{
  "id": "WHATSAPP-BUSINESS-ACCOUNT-ID",
  "name": "Test WhatsApp Business Account",
  "timezone\_id": "1",
  "message\_template\_namespace": "MESSAGE-TEMPLATE-NAMESPACE"
}